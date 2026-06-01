"""
Android package name lookup tool — PySide6 GUI.

Features:
- Single package lookup (exact match → LIKE fallback)
- CSV batch import / export
- Manual app name overrides
- Drag & drop CSV files
- Fully offline with a local SQLite database
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QTableView,
    QVBoxLayout,
    QWidget,
    QAbstractItemView,
)

if TYPE_CHECKING:
    from PySide6.QtGui import QDragEnterEvent, QDropEvent

from database import AppDatabase
from import_export import CSV_COLUMNS_EXPORT, export_csv, import_csv

# ---------------------------------------------------------------------------
# Model column indices (display columns)
# ---------------------------------------------------------------------------
COL_INDEX = 0
COL_PACKAGE = 1
COL_APP_NAME = 2
COL_STATUS = 3

HEADERS = ["序号", "包名", "应用名", "状态"]

# Row background colours
COLOR_FOUND = QColor("#E0FFE0")       # light green
COLOR_NOT_FOUND = QColor("#FFE0E0")   # light red
# Status text colours
COLOR_STATUS_FOUND = QColor("#2E7D32")      # dark green
COLOR_STATUS_NOT_FOUND = QColor("#C62828")  # dark red


# ======================================================================
# Table Model
# ======================================================================

class PackageTableModel(QAbstractTableModel):
    """Custom table model holding query results.

    Each row is a dict::

        {"package_name": str, "app_name": str | None, "found": bool}
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._rows: list[dict] = []

    # --- QAbstractTableModel interface ---------------------------------

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._rows)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(HEADERS)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        row = self._rows[index.row()]
        col = index.column()

        # --- Display ----------------------------------------------------
        if role == Qt.DisplayRole:
            if col == COL_INDEX:
                return str(index.row() + 1)
            elif col == COL_PACKAGE:
                return row["package_name"]
            elif col == COL_APP_NAME:
                if row["found"] and row["app_name"]:
                    return row["app_name"]
                return "(未找到)"
            elif col == COL_STATUS:
                return "✓ 已识别" if row["found"] else "✗ 未识别"

        # --- Background colour ------------------------------------------
        elif role == Qt.BackgroundRole:
            return QBrush(COLOR_FOUND if row["found"] else COLOR_NOT_FOUND)

        # --- Foreground colour (status column) --------------------------
        elif role == Qt.ForegroundRole:
            if col == COL_STATUS:
                return QBrush(
                    COLOR_STATUS_FOUND if row["found"] else COLOR_STATUS_NOT_FOUND
                )

        # --- Text alignment ---------------------------------------------
        elif role == Qt.TextAlignmentRole:
            if col in (COL_INDEX, COL_STATUS):
                return Qt.AlignCenter

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole
    ):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(HEADERS):
                return HEADERS[section]
        return None

    # --- Public methods -------------------------------------------------

    def add_row(
        self,
        package_name: str,
        app_name: str | None = None,
        found: bool = False,
    ) -> None:
        """Append a single row to the model."""
        row_idx = len(self._rows)
        self.beginInsertRows(QModelIndex(), row_idx, row_idx)
        self._rows.append(
            {"package_name": package_name, "app_name": app_name, "found": found}
        )
        self.endInsertRows()

    def set_rows(self, rows: list[dict]) -> None:
        """Replace all rows in the model."""
        self.beginResetModel()
        self._rows = list(rows)
        self.endResetModel()

    def clear(self) -> None:
        """Remove every row."""
        self.beginResetModel()
        self._rows.clear()
        self.endResetModel()

    def update_row(
        self,
        row_idx: int,
        package_name: str,
        app_name: str,
        found: bool = True,
    ) -> None:
        """Update a single row in-place and emit ``dataChanged``."""
        if 0 <= row_idx < len(self._rows):
            self._rows[row_idx] = {
                "package_name": package_name,
                "app_name": app_name,
                "found": found,
            }
            top_left = self.index(row_idx, 0)
            bottom_right = self.index(row_idx, len(HEADERS) - 1)
            self.dataChanged.emit(top_left, bottom_right, [Qt.DisplayRole])

    def get_row(self, row_idx: int) -> dict | None:
        """Return a copy of the row dict, or *None* if out of range."""
        if 0 <= row_idx < len(self._rows):
            return dict(self._rows[row_idx])
        return None

    def get_all_rows(self) -> list[dict]:
        """Return a shallow copy of all rows."""
        return [dict(r) for r in self._rows]

    # --- Convenience properties -----------------------------------------

    @property
    def total_count(self) -> int:
        return len(self._rows)

    @property
    def found_count(self) -> int:
        return sum(1 for r in self._rows if r["found"])

    @property
    def not_found_count(self) -> int:
        return sum(1 for r in self._rows if not r["found"])


# ======================================================================
# Manual-Add Dialog
# ======================================================================

class ManualAddDialog(QDialog):
    """Dialog for manually adding or overriding an app name for a package."""

    def __init__(
        self,
        package_name: str,
        current_app_name: str = "",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("手动添加应用名")
        self.setMinimumWidth(420)

        layout = QFormLayout(self)

        # Package name — read-only, selectable for copy
        pkg_label = QLabel(package_name)
        pkg_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pkg_label.setStyleSheet("font-family: monospace;")
        layout.addRow("包名:", pkg_label)

        # App name — editable
        self._app_name_edit = QLineEdit(current_app_name)
        self._app_name_edit.setPlaceholderText("输入应用名…")
        layout.addRow("应用名:", self._app_name_edit)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def app_name(self) -> str:
        """Return the entered app name, stripped of whitespace."""
        return self._app_name_edit.text().strip()


# ======================================================================
# Main Window
# ======================================================================

class MainWindow(QMainWindow):
    """Top-level window for the Android package name lookup tool."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Android 包名识别工具")
        self.resize(1000, 600)
        self.setAcceptDrops(True)

        # --- Database ---------------------------------------------------
        self._db = AppDatabase()

        # --- Model ------------------------------------------------------
        self._model = PackageTableModel(self)

        # --- Build UI ---------------------------------------------------
        self._setup_ui()
        self._update_status_bar()
        self._center_on_screen()

    # ==================================================================
    # UI Construction
    # ==================================================================

    def _setup_ui(self) -> None:
        """Create and arrange all widgets."""
        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(8)

        # ---- Toolbar ----------------------------------------------------
        toolbar = QHBoxLayout()
        toolbar.setSpacing(6)

        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("输入包名，如 com.tencent.mm")
        self._search_input.returnPressed.connect(self._on_search)
        toolbar.addWidget(self._search_input, stretch=1)

        self._btn_search = QPushButton("搜索")
        self._btn_search.setDefault(True)
        self._btn_search.clicked.connect(self._on_search)
        toolbar.addWidget(self._btn_search)

        self._btn_import = QPushButton("导入CSV")
        self._btn_import.clicked.connect(self._on_import)
        toolbar.addWidget(self._btn_import)

        self._btn_export = QPushButton("导出CSV")
        self._btn_export.clicked.connect(self._on_export)
        toolbar.addWidget(self._btn_export)

        self._btn_clear = QPushButton("清空")
        self._btn_clear.clicked.connect(self._on_clear)
        toolbar.addWidget(self._btn_clear)

        root.addLayout(toolbar)

        # ---- Table ------------------------------------------------------
        self._table = QTableView()
        self._table.setModel(self._model)
        self._table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._table.setSelectionMode(QAbstractItemView.SingleSelection)
        self._table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._table.setAlternatingRowColors(False)
        self._table.verticalHeader().setVisible(False)
        self._table.setContextMenuPolicy(Qt.CustomContextMenu)
        self._table.customContextMenuRequested.connect(self._on_context_menu)

        # Column sizing
        hdr = self._table.horizontalHeader()
        hdr.setSectionResizeMode(COL_INDEX, QHeaderView.Fixed)
        hdr.resizeSection(COL_INDEX, 50)
        hdr.setSectionResizeMode(COL_PACKAGE, QHeaderView.Stretch)
        hdr.setSectionResizeMode(COL_APP_NAME, QHeaderView.Fixed)
        hdr.resizeSection(COL_APP_NAME, 200)
        hdr.setSectionResizeMode(COL_STATUS, QHeaderView.Fixed)
        hdr.resizeSection(COL_STATUS, 80)

        root.addWidget(self._table, stretch=1)

        # ---- Status bar -------------------------------------------------
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._status_label = QLabel()
        self._status_bar.addPermanentWidget(self._status_label)

    # ==================================================================
    # Search
    # ==================================================================

    def _on_search(self) -> None:
        """Execute a single package search (exact → LIKE fallback)."""
        query = self._search_input.text().strip()
        if not query:
            return

        # 1. Exact match
        result = self._db.search(query)
        if result is not None:
            self._model.add_row(
                package_name=result["package_name"],
                app_name=result["app_name"],
                found=True,
            )
            self._table.scrollToBottom()
            self._update_status_bar()
            self._search_input.clear()
            return

        # 2. LIKE fallback — show up to 10 similar matches
        similar = self._db.search_like(query, limit=10)
        if similar:
            for row in similar:
                self._model.add_row(
                    package_name=row["package_name"],
                    app_name=row["app_name"],
                    found=True,
                )
            self._table.scrollToBottom()
            self._update_status_bar()
            self._search_input.clear()
            return

        # 3. Nothing found
        self._model.add_row(package_name=query, app_name=None, found=False)
        self._table.scrollToBottom()
        self._update_status_bar()
        self._search_input.clear()

    # ==================================================================
    # CSV Import (button + drag-drop)
    # ==================================================================

    def _on_import(self) -> None:
        """Open a file dialog and import a CSV file."""
        filepath, _ = QFileDialog.getOpenFileName(
            self,
            "选择CSV文件",
            "",
            "CSV 文件 (*.csv);;所有文件 (*)",
        )
        if filepath:
            self._import_csv_file(filepath)

    def _import_csv_file(self, filepath: str) -> None:
        """Shared import logic used by both the button and drag-drop.

        Reads the CSV via :func:`import_csv`, then queries the database
        for any packages that do not already have an *app_name* in the
        CSV.  Rows with a pre-filled *app_name* skip the DB lookup and
        are upserted into the local database so future lookups are fast.
        """
        try:
            records = import_csv(filepath)
        except ValueError as exc:
            QMessageBox.critical(self, "导入失败", str(exc))
            return

        if not records:
            QMessageBox.information(self, "导入", "CSV 文件中没有数据。")
            return

        need_lookup: list[str] = []

        for rec in records:
            pkg = rec["package_name"]
            app = rec.get("app_name", "").strip()
            if app:
                # CSV already had an app name — use it directly
                self._model.add_row(package_name=pkg, app_name=app, found=True)
                # Persist to the local DB for future queries
                self._db.upsert(package_name=pkg, app_name=app)
            else:
                need_lookup.append(pkg)

        # Batch-lookup packages that had no pre-filled name
        if need_lookup:
            found_map: dict[str, str] = {}
            db_rows = self._db.search_batch(need_lookup)
            for row in db_rows:
                found_map[row["package_name"]] = row["app_name"]

            for pkg in need_lookup:
                if pkg in found_map:
                    self._model.add_row(
                        package_name=pkg, app_name=found_map[pkg], found=True
                    )
                else:
                    self._model.add_row(package_name=pkg, app_name=None, found=False)

        self._table.scrollToBottom()
        self._update_status_bar()

    # ==================================================================
    # CSV Export
    # ==================================================================

    def _on_export(self) -> None:
        """Export the current table contents to a CSV file."""
        if self._model.total_count == 0:
            QMessageBox.information(self, "导出", "表格中没有数据可导出。")
            return

        filepath, _ = QFileDialog.getSaveFileName(
            self,
            "导出CSV",
            "export.csv",
            "CSV 文件 (*.csv);;所有文件 (*)",
        )
        if not filepath:
            return

        # Build export rows matching the columns from import_export
        rows: list[dict] = []
        for r in self._model.get_all_rows():
            rows.append(
                {
                    "package_name": r["package_name"],
                    "app_name": r["app_name"] if r["found"] else "",
                    # status is auto-computed by export_csv()
                }
            )

        try:
            export_csv(filepath, rows, columns=CSV_COLUMNS_EXPORT)
            self._status_bar.showMessage(f"已导出到: {filepath}", 5000)
        except OSError as exc:
            QMessageBox.critical(self, "导出失败", f"写入文件失败:\n{exc}")

    # ==================================================================
    # Clear
    # ==================================================================

    def _on_clear(self) -> None:
        """Clear all rows from the table."""
        self._model.clear()
        self._update_status_bar()

    # ==================================================================
    # Status bar
    # ==================================================================

    def _update_status_bar(self) -> None:
        """Update the permanent status-bar widget with row / DB counts."""
        db_total = self._db.count()

        message = (
            f"共 {self._model.total_count} 条 | "
            f"已识别 {self._model.found_count} | "
            f"未识别 {self._model.not_found_count} | "
            f"数据库共 {db_total:,} 条"
        )

        if db_total == 0:
            message += (
                "  ⚠ 数据库为空 — 请先运行爬虫（scrapers/）填充数据"
            )

        self._status_label.setText(message)

    # ==================================================================
    # Right-click context menu
    # ==================================================================

    def _on_context_menu(self, pos) -> None:
        """Show a context menu on the table with copy / manual-add actions."""
        index = self._table.indexAt(pos)
        if not index.isValid():
            return

        row_idx = index.row()
        row_data = self._model.get_row(row_idx)
        if row_data is None:
            return

        menu = QMenu(self)

        copy_action = menu.addAction("复制包名")
        copy_action.triggered.connect(
            lambda: self._copy_package_name(row_data["package_name"])
        )

        manual_action = menu.addAction("手动添加")
        manual_action.triggered.connect(lambda: self._manual_add(row_idx))

        menu.exec(self._table.viewport().mapToGlobal(pos))

    def _copy_package_name(self, package_name: str) -> None:
        """Copy *package_name* to the system clipboard."""
        clipboard = QApplication.clipboard()
        if clipboard is not None:
            clipboard.setText(package_name)

    def _manual_add(self, row_idx: int) -> None:
        """Open the manual-add dialog and persist the result."""
        row_data = self._model.get_row(row_idx)
        if row_data is None:
            return

        current_name = row_data["app_name"] if (row_data["found"] and row_data["app_name"]) else ""

        dialog = ManualAddDialog(
            package_name=row_data["package_name"],
            current_app_name=current_name,
            parent=self,
        )
        if dialog.exec() == QDialog.Accepted:
            new_name = dialog.app_name()
            if not new_name:
                QMessageBox.warning(self, "警告", "应用名不能为空。")
                return

            # Persist
            self._db.upsert(
                package_name=row_data["package_name"],
                app_name=new_name,
                source="manual",
            )

            # Refresh the table row
            self._model.update_row(
                row_idx, row_data["package_name"], new_name, found=True
            )
            self._update_status_bar()

    # ==================================================================
    # Drag & drop
    # ==================================================================

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        """Accept drag events that contain at least one ``.csv`` file."""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                if url.toLocalFile().lower().endswith(".csv"):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        """Handle a dropped CSV file — import the first valid one."""
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                filepath = url.toLocalFile()
                if filepath.lower().endswith(".csv"):
                    self._import_csv_file(filepath)
                    break  # one file per drop

    # ==================================================================
    # Helpers
    # ==================================================================

    def _center_on_screen(self) -> None:
        """Position the window in the centre of the primary screen."""
        screen = QApplication.primaryScreen()
        if screen is not None:
            geo = screen.availableGeometry()
            self.move(
                (geo.width() - self.width()) // 2 + geo.x(),
                (geo.height() - self.height()) // 2 + geo.y(),
            )


# ======================================================================
# Entry point
# ======================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # cross-platform consistent look
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
