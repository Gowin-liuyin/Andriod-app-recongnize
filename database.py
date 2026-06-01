"""
SQLite database module for Android package name lookup.

Provides the AppDatabase class — the single source of truth for all
package-to-app-name lookups.  All other modules (scrapers, web UI, CLI)
depend on this module.
"""

import sqlite3
import os
import threading


class AppDatabase:
    """Thread-safe SQLite database for Android app metadata.

    The database file is created automatically on first use.  All writes
    use WAL mode for better concurrent read/write performance.
    """

    def __init__(self, db_path: str | None = None):
        """
        Parameters
        ----------
        db_path : str or None
            Path to the SQLite database file.  Defaults to ``apps.db``
            in the same directory as this module.
        """
        if db_path is None:
            db_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "apps.db"
            )

        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self._lock = threading.Lock()
        self._create_tables()

    # ------------------------------------------------------------------
    # Schema
    # ------------------------------------------------------------------

    def _create_tables(self) -> None:
        """Create tables and indexes if they do not already exist."""
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS apps (
                package_name TEXT PRIMARY KEY,
                app_name     TEXT NOT NULL,
                app_name_en  TEXT,
                developer    TEXT,
                category     TEXT,
                installs     TEXT,
                score        REAL,
                source       TEXT DEFAULT 'play_store',
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_package   ON apps(package_name);
            CREATE INDEX IF NOT EXISTS idx_developer ON apps(developer);
            CREATE INDEX IF NOT EXISTS idx_app_name  ON apps(app_name);
            """
        )
        self.conn.commit()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def upsert(
        self,
        package_name: str,
        app_name: str,
        app_name_en: str | None = None,
        developer: str | None = None,
        category: str | None = None,
        installs: str | None = None,
        score: float | None = None,
        source: str = "play_store",
    ) -> bool:
        """Insert a new row or update an existing one.

        If *package_name* already exists, only columns where the new
        value is **not** ``None`` are overwritten (existing data is
        preserved for ``None`` arguments).  For new rows every column
        is set — ``None`` values become ``NULL``.

        Returns ``True`` when a new row was inserted, ``False`` when an
        existing row was updated.
        """
        with self._lock:
            existing = self.conn.execute(
                "SELECT 1 FROM apps WHERE package_name = ?", (package_name,)
            ).fetchone()

            if existing is None:
                # --- INSERT -------------------------------------------------
                self.conn.execute(
                    """
                    INSERT INTO apps (
                        package_name, app_name, app_name_en, developer,
                        category, installs, score, source
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        package_name,
                        app_name,
                        app_name_en,
                        developer,
                        category,
                        installs,
                        score,
                        source,
                    ),
                )
                self.conn.commit()
                return True
            else:
                # --- UPDATE -------------------------------------------------
                set_clauses = []
                params: list = []

                if app_name is not None:
                    set_clauses.append("app_name = ?")
                    params.append(app_name)
                if app_name_en is not None:
                    set_clauses.append("app_name_en = ?")
                    params.append(app_name_en)
                if developer is not None:
                    set_clauses.append("developer = ?")
                    params.append(developer)
                if category is not None:
                    set_clauses.append("category = ?")
                    params.append(category)
                if installs is not None:
                    set_clauses.append("installs = ?")
                    params.append(installs)
                if score is not None:
                    set_clauses.append("score = ?")
                    params.append(score)
                if source is not None:
                    set_clauses.append("source = ?")
                    params.append(source)

                if set_clauses:
                    set_clauses.append("updated_at = CURRENT_TIMESTAMP")
                    params.append(package_name)
                    self.conn.execute(
                        f"UPDATE apps SET {', '.join(set_clauses)} "
                        "WHERE package_name = ?",
                        params,
                    )
                    self.conn.commit()
                return False

    def upsert_batch(self, records: list[dict]) -> int:
        """Insert or update many rows in a single transaction.

        Uses ``executemany`` for performance.  Each dict must contain at
        least ``package_name`` and ``app_name``.  Missing keys default
        to ``None`` (or ``'play_store'`` for *source*).

        Returns the number of rows affected (inserted or updated).
        """
        if not records:
            return 0

        with self._lock:
            cursor = self.conn.executemany(
                """
                INSERT INTO apps (
                    package_name, app_name, app_name_en, developer,
                    category, installs, score, source
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(package_name) DO UPDATE SET
                    app_name    = COALESCE(excluded.app_name,    apps.app_name),
                    app_name_en = COALESCE(excluded.app_name_en, apps.app_name_en),
                    developer   = COALESCE(excluded.developer,   apps.developer),
                    category    = COALESCE(excluded.category,    apps.category),
                    installs    = COALESCE(excluded.installs,    apps.installs),
                    score       = COALESCE(excluded.score,       apps.score),
                    source      = COALESCE(excluded.source,      apps.source),
                    updated_at  = CURRENT_TIMESTAMP
                """,
                [
                    (
                        r["package_name"],
                        r["app_name"],
                        r.get("app_name_en"),
                        r.get("developer"),
                        r.get("category"),
                        r.get("installs"),
                        r.get("score"),
                        r.get("source", "play_store"),
                    )
                    for r in records
                ],
            )
            self.conn.commit()
            return cursor.rowcount

    def search(self, package_name: str) -> dict | None:
        """Look up a single package by its exact package name.

        Returns the full row as a ``dict``, or ``None`` when not found.
        """
        row = self.conn.execute(
            "SELECT * FROM apps WHERE package_name = ?", (package_name,)
        ).fetchone()
        return dict(row) if row else None

    def search_batch(self, package_names: list[str]) -> list[dict]:
        """Look up multiple packages by exact package name.

        Returns a list of dicts for **found** packages only — missing
        packages are silently omitted from the result.
        """
        if not package_names:
            return []

        placeholders = ",".join("?" for _ in package_names)
        rows = self.conn.execute(
            f"SELECT * FROM apps WHERE package_name IN ({placeholders})",
            package_names,
        ).fetchall()
        return [dict(r) for r in rows]

    def search_like(self, keyword: str, limit: int = 50) -> list[dict]:
        """Fuzzy search on both *package_name* and *app_name*.

        The *keyword* is wrapped with ``%`` wildcards so partial matches
        work.  Results are ordered so exact package-name matches appear
        first, then app-name matches.
        """
        pattern = f"%{keyword}%"
        rows = self.conn.execute(
            """
            SELECT * FROM apps
             WHERE package_name LIKE ?
                OR app_name LIKE ?
             ORDER BY
                 CASE WHEN package_name = ? THEN 0 ELSE 1 END,
                 package_name
             LIMIT ?
            """,
            (pattern, pattern, keyword, limit),
        ).fetchall()
        return [dict(r) for r in rows]

    def count(self) -> int:
        """Return the total number of rows in the database."""
        row = self.conn.execute("SELECT COUNT(*) FROM apps").fetchone()
        return row[0] if row else 0

    def close(self) -> None:
        """Close the database connection."""
        try:
            self.conn.close()
        except sqlite3.Error:
            pass


# ----------------------------------------------------------------------
# Self-test (run with: python database.py)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    import tempfile

    # Use a temporary file so we don't pollute the real database.
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tf:
        test_db_path = tf.name

    try:
        db = AppDatabase(test_db_path)

        # ---------- single insert ----------
        inserted = db.upsert(
            package_name="com.tencent.mm",
            app_name="微信",
            app_name_en="WeChat",
            developer="Tencent",
            category="Social",
            installs="1,000,000,000+",
            score=4.3,
        )
        assert inserted is True, "Expected new row inserted"
        print("PASS: upsert inserted a new row")

        # ---------- single update (only score) ----------
        updated = db.upsert(
            package_name="com.tencent.mm",
            app_name=None,
            score=4.5,
        )
        assert updated is False, "Expected existing row updated"
        row = db.search("com.tencent.mm")
        assert row["score"] == 4.5, "Score should be updated"
        assert row["app_name"] == "微信", "app_name should be unchanged"
        print("PASS: upsert updated only the score, left app_name alone")

        # ---------- search miss ----------
        assert db.search("com.does.not.exist") is None
        print("PASS: search returns None for missing package")

        # ---------- batch upsert ----------
        records = [
            {
                "package_name": "com.android.chrome",
                "app_name": "Chrome",
                "developer": "Google",
                "score": 4.2,
            },
            {
                "package_name": "com.spotify.music",
                "app_name": "Spotify",
                "developer": "Spotify AB",
                "installs": "500,000,000+",
            },
            {
                "package_name": "com.tencent.mm",  # update existing
                "app_name": "微信",
                "score": 4.6,
            },
        ]
        affected = db.upsert_batch(records)
        assert affected == 3, f"Expected 3 affected, got {affected}"
        print(f"PASS: batch upsert affected {affected} rows")

        # ---------- search_batch ----------
        results = db.search_batch(
            ["com.android.chrome", "com.spotify.music", "com.missing.one"]
        )
        assert len(results) == 2, f"Expected 2 found, got {len(results)}"
        print("PASS: search_batch returned only found packages")

        # ---------- search_like ----------
        like_results = db.search_like("chrome")
        assert any(
            r["package_name"] == "com.android.chrome" for r in like_results
        ), "search_like should find Chrome"
        print("PASS: search_like found matching packages")

        # ---------- count ----------
        total = db.count()
        assert total == 3, f"Expected 3 total rows, got {total}"
        print(f"PASS: count = {total}")

        # ---------- Chinese / English name handling ----------
        db.upsert(
            package_name="com.example.bilingual",
            app_name="示例",
            app_name_en="Example",
        )
        row = db.search("com.example.bilingual")
        assert row["app_name"] == "示例"
        assert row["app_name_en"] == "Example"
        print("PASS: bilingual app name stored correctly")

        # ---------- source defaults ----------
        assert row["source"] == "play_store", "Default source should be play_store"
        print("PASS: source defaults to play_store")

        db.close()
        print("\nAll tests passed.")

    finally:
        os.unlink(test_db_path)
