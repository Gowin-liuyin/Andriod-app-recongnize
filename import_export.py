"""CSV import/export logic for Android package name lookup tool.

Provides two functions — import_csv and export_csv — plus column constants
for consistent CSV handling across the application. Supports UTF-8, UTF-8-BOM,
GBK, and GB2312 encodings on import, and always writes UTF-8-BOM on export for
Excel compatibility.
"""

from __future__ import annotations

import csv
import os
import tempfile
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CSV_COLUMNS_DEFAULT = ["package_name", "app_name", "developer", "category", "status"]
"""Default columns used when exporting results if none are specified."""

CSV_COLUMNS_EXPORT = [
    "package_name",
    "app_name",
    "app_name_en",
    "developer",
    "category",
    "installs",
    "score",
    "status",
]
"""Full set of export columns available to callers."""

# Order matters: try utf-8-sig first so BOM files are handled cleanly, then
# plain UTF-8, then the Chinese legacy encodings.
_ENCODINGS = ("utf-8-sig", "utf-8", "gbk", "gb2312")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_package_column(fieldnames: list[str]) -> str:
    """Return the field name most likely to hold a package identifier.

    Resolution order
    ----------------
    1. Exact (case-insensitive) match on ``"package_name"``.
    2. First column whose name contains ``"package"`` or ``"pkg"``.
    3. First column overall (assumed to be the package name).
    4. Literal ``"package_name"`` when *fieldnames* is empty (should not
       happen in practice; the caller guards against zero rows).
    """
    if not fieldnames:
        return "package_name"

    lower_map = {name: name.lower().strip() for name in fieldnames}

    # 1 – exact match
    for name in fieldnames:
        if lower_map[name] == "package_name":
            return name

    # 2 – fuzzy match
    for name in fieldnames:
        low = lower_map[name]
        if "package" in low or "pkg" in low:
            return name

    # 3 – first column
    return fieldnames[0]


def _try_read_csv(file_path: str, encoding: str) -> list[dict]:
    """Attempt to read *file_path* with the given *encoding*.

    Returns the list of rows on success.  Raises :exc:`UnicodeError` on
    decode failures so the caller can try the next encoding.
    """
    with open(file_path, "r", encoding=encoding, newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def import_csv(file_path: str) -> list[dict]:
    """Read a CSV file from disk and return rows as dicts.

    The column containing the package name is auto-detected (see
    :func:`_find_package_column`) and normalized to the key
    ``"package_name"`` in every returned dict.  All other columns are
    preserved as-is.

    Encoding is auto-detected by attempting UTF-8 (with and without BOM),
    GBK, and GB2312 in order.

    Args:
        file_path: Absolute or relative path to the CSV file.

    Returns:
        A list of dicts.  Every dict is guaranteed to have a
        ``"package_name"`` key.  Returns an empty list when the file
        exists but contains zero data rows.

    Raises:
        ValueError: If *file_path* does not exist or cannot be decoded
            with any of the supported encodings.
    """
    if not os.path.isfile(file_path):
        raise ValueError(f"File not found: {file_path!r}")

    rows: list[dict] = []
    last_error: Exception | None = None

    for encoding in _ENCODINGS:
        try:
            rows = _try_read_csv(file_path, encoding)
            break
        except (UnicodeDecodeError, UnicodeError) as exc:
            last_error = exc
            continue
    else:
        raise ValueError(
            f"Unable to decode {file_path!r} with any supported encoding "
            f"({', '.join(_ENCODINGS)}). Last error: {last_error}"
        ) from last_error

    # Empty file (header-only or truly empty) — nothing to normalise.
    if not rows:
        return []

    fieldnames = list(rows[0].keys())
    pkg_col = _find_package_column(fieldnames)

    # Normalise every row so the package-name key is always "package_name".
    if pkg_col == "package_name":
        return rows

    result: list[dict] = []
    for row in rows:
        item = dict(row)
        item["package_name"] = item.pop(pkg_col, "")
        result.append(item)

    return result


def export_csv(
    file_path: str,
    results: list[dict],
    columns: Optional[list[str]] = None,
) -> None:
    """Write lookup results to a CSV file.

    The file is always written with UTF-8-BOM encoding so that Microsoft
    Excel can open it directly without mangling non-ASCII characters.

    The ``"status"`` column is populated automatically from ``app_name``:
    ``"已识别"`` when *app_name* is truthy, otherwise ``"未识别"``.  Any
    pre-existing value in the row is overwritten.

    Args:
        file_path: Destination path.  Intermediate directories are created
            if they do not exist.
        results: One dict per row.  Keys that are not in *columns* are
            silently dropped.
        columns: Column names and order for the output CSV.  Defaults to
            :data:`CSV_COLUMNS_DEFAULT`.

    Raises:
        OSError: If the file cannot be written (permission denied, invalid
            path, …).  These exceptions are allowed to propagate so the
            caller can decide how to handle them.
    """
    if columns is None:
        columns = CSV_COLUMNS_DEFAULT

    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()

        for row in results:
            # Start with a clean row containing only the requested columns.
            out_row: dict[str, str] = {col: row.get(col, "") for col in columns}

            # Auto-compute the status column from app_name.
            if "status" in columns:
                app_name = out_row.get("app_name", "")
                out_row["status"] = "已识别" if app_name else "未识别"

            writer.writerow(out_row)


# ---------------------------------------------------------------------------
# Self-test (run with: python -m import_export or python import_export.py)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    test_rows = [
        {
            "package_name": "com.tencent.mm",
            "app_name": "微信",
            "developer": "Tencent",
            "category": "Social",
        },
        {
            "package_name": "com.example.foo",
            "app_name": "",
            "developer": "",
            "category": "",
        },
        {
            "package_name": "com.test.bar",
            "app_name": "Bar App",
            "developer": "DevCo",
            "category": "Tools",
        },
    ]

    temp_files: list[str] = []

    def _temp_csv(suffix: str = ".csv") -> str:
        """Create a named temporary file and track it for cleanup."""
        fd, path = tempfile.mkstemp(suffix=suffix)
        os.close(fd)
        temp_files.append(path)
        return path

    try:
        # ----------------------------------------------------------------
        # Test 1 – basic import
        # ----------------------------------------------------------------
        path1 = _temp_csv()
        with open(path1, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["package_name", "app_name", "developer", "category"])
            w.writeheader()
            w.writerows(test_rows)

        imported = import_csv(path1)
        assert len(imported) == 3, f"expected 3 rows, got {len(imported)}"
        assert imported[0]["package_name"] == "com.tencent.mm"
        assert imported[1]["package_name"] == "com.example.foo"
        assert imported[2]["package_name"] == "com.test.bar"
        print("Test 1 (basic import): PASSED")

        # ----------------------------------------------------------------
        # Test 2 – export round-trip with status auto-computation
        # ----------------------------------------------------------------
        path2 = _temp_csv()
        export_csv(path2, imported)

        reimported = import_csv(path2)
        assert len(reimported) == 3
        assert reimported[0]["status"] == "已识别"  # 微信
        assert reimported[1]["status"] == "未识别"  # empty app_name
        assert reimported[2]["status"] == "已识别"  # Bar App
        # Verify all expected columns are present.
        for col in CSV_COLUMNS_DEFAULT:
            assert col in reimported[0], f"missing column {col!r}"
        print("Test 2 (export round-trip + status): PASSED")

        # ----------------------------------------------------------------
        # Test 3 – fuzzy column detection (column contains "pkg")
        # ----------------------------------------------------------------
        path3 = _temp_csv()
        with open(path3, "w", encoding="utf-8", newline="") as fh:
            fh.write("name,id,pkg_name\n")
            fh.write("Bar,123,com.fuzzy.test\n")

        imported_fuzzy = import_csv(path3)
        assert len(imported_fuzzy) == 1
        assert imported_fuzzy[0]["package_name"] == "com.fuzzy.test"
        print("Test 3 (fuzzy column detect): PASSED")

        # ----------------------------------------------------------------
        # Test 4 – first-column fallback (no "package" or "pkg" column)
        # ----------------------------------------------------------------
        path4 = _temp_csv()
        with open(path4, "w", encoding="utf-8", newline="") as fh:
            fh.write("col_a,col_b,col_c\n")
            fh.write("com.first.col,value_b,value_c\n")

        imported_first = import_csv(path4)
        assert len(imported_first) == 1
        assert imported_first[0]["package_name"] == "com.first.col"
        assert imported_first[0]["col_b"] == "value_b"
        print("Test 4 (first-column fallback): PASSED")

        # ----------------------------------------------------------------
        # Test 5 – empty file
        # ----------------------------------------------------------------
        path5 = _temp_csv()
        # File is just created, zero bytes.
        imported_empty = import_csv(path5)
        assert imported_empty == []
        print("Test 5 (empty file): PASSED")

        # ----------------------------------------------------------------
        # Test 6 – header-only file (no data rows)
        # ----------------------------------------------------------------
        path6 = _temp_csv()
        with open(path6, "w", encoding="utf-8", newline="") as fh:
            fh.write("package_name,app_name\n")
        imported_header_only = import_csv(path6)
        assert imported_header_only == []
        print("Test 6 (header-only file): PASSED")

        # ----------------------------------------------------------------
        # Test 7 – custom columns on export
        # ----------------------------------------------------------------
        path7 = _temp_csv()
        export_csv(path7, imported, columns=["package_name", "app_name", "status"])
        custom_imported = import_csv(path7)
        assert set(custom_imported[0].keys()) == {"package_name", "app_name", "status"}
        assert custom_imported[0]["status"] == "已识别"
        print("Test 7 (custom columns): PASSED")

        # ----------------------------------------------------------------
        # Test 8 – GBK encoding
        # ----------------------------------------------------------------
        path8 = _temp_csv()
        with open(path8, "w", encoding="gbk", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["包名", "应用名"])
            w.writeheader()
            w.writerow({"包名": "com.gbk.test", "应用名": "测试应用"})

        imported_gbk = import_csv(path8)
        assert len(imported_gbk) == 1
        assert imported_gbk[0]["package_name"] == "com.gbk.test"
        assert imported_gbk[0]["应用名"] == "测试应用"
        print("Test 8 (GBK encoding): PASSED")

        # ----------------------------------------------------------------
        # Test 9 – missing file raises ValueError
        # ----------------------------------------------------------------
        try:
            import_csv("/tmp/nonexistent_package_lookup_test.csv")
            assert False, "should have raised ValueError"
        except ValueError as exc:
            assert "not found" in str(exc).lower() or "nonexistent" in str(exc)
        print("Test 9 (missing file raises ValueError): PASSED")

        # ----------------------------------------------------------------
        # Test 10 – UTF-8-BOM handling
        # ----------------------------------------------------------------
        path10 = _temp_csv()
        with open(path10, "w", encoding="utf-8-sig", newline="") as fh:
            fh.write("package_name,app_name\n")
            fh.write("com.bom.test,BOM Test\n")

        imported_bom = import_csv(path10)
        assert len(imported_bom) == 1
        assert imported_bom[0]["package_name"] == "com.bom.test"
        # The BOM must NOT leak into the column name.
        assert "﻿" not in imported_bom[0].get("package_name", "")
        print("Test 10 (UTF-8-BOM): PASSED")

        print("\nAll tests passed!")

    finally:
        # Clean up every temporary file we created.
        for p in temp_files:
            try:
                os.unlink(p)
            except OSError:
                pass
