import os
import csv

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QFrame
)
from PySide6.QtCore import Qt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "final_prediction_dataset.csv")


class ChildHistoryPage(QWidget):
    def __init__(self):
        super().__init__()

        self.records = self.load_data()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)

        title = QLabel("🧒 Child History")
        title.setStyleSheet("font-size:32px; font-weight:800; color:#0D47A1;")

        subtitle = QLabel("Search a child by ID and view complete nutrition monitoring history.")
        subtitle.setStyleSheet("font-size:16px; color:#456A7A;")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        search_box = QFrame()
        search_box.setStyleSheet("""
            QFrame {
                background:#E3F2FD;
                border-radius:20px;
                padding:14px;
            }
        """)

        search_layout = QHBoxLayout(search_box)

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter Child ID")
        self.id_input.setStyleSheet("""
            QLineEdit {
                background:white;
                border:2px solid #B3E5FC;
                border-radius:14px;
                padding:12px;
                font-size:16px;
            }
        """)

        search_btn = QPushButton("🔍 Search")
        search_btn.setStyleSheet("""
            QPushButton {
                background:#4FC3F7;
                color:white;
                border:none;
                border-radius:14px;
                padding:12px 24px;
                font-size:16px;
                font-weight:700;
            }
            QPushButton:hover {
                background:#29B6F6;
            }
        """)
        search_btn.clicked.connect(self.search_child)

        search_layout.addWidget(self.id_input)
        search_layout.addWidget(search_btn)

        layout.addWidget(search_box)

        self.info_label = QLabel("👶 Enter a child ID to view records.")
        self.info_label.setStyleSheet("""
            background:#FFF8E1;
            padding:12px;
            border-radius:14px;
            font-size:15px;
            color:#4E6570;
        """)
        layout.addWidget(self.info_label)

        self.table = QTableWidget()
        self.table.setStyleSheet("""
            QTableWidget {
                background:white;
                border-radius:16px;
                border:1px solid #BDEBFF;
                font-size:14px;
            }
            QHeaderView::section {
                background:#81D4FA;
                color:#003B5C;
                padding:8px;
                font-weight:bold;
                border:none;
            }
        """)

        layout.addWidget(self.table)

    def load_data(self):
        records = []

        if not os.path.exists(DATA_FILE):
            return records

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)

        return records

    def search_child(self):
        child_id = self.id_input.text().strip()

        if not child_id:
            self.info_label.setText("⚠️ Please enter a Child ID.")
            return

        child_records = [
            row for row in self.records
            if str(row.get("ID", "")).strip() == child_id
        ]

        if not child_records:
            self.info_label.setText("❌ No records found for this Child ID.")
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            return

        child_records = sorted(child_records, key=lambda x: x.get("GmpDate", ""))

        name = child_records[-1].get("Name", "N/A")
        condition = child_records[-1].get("Condition", "N/A")
        muac = child_records[-1].get("MUAC", "N/A")

        self.info_label.setText(
            f"👶 Child ID: {child_id} | Name: {name} | Latest MUAC: {muac} | Current Condition: {condition}"
        )

        columns = [
            "GmpDate",
            "Age_Months",
            "MUAC",
            "Previous_MUAC",
            "MUAC_Change",
            "Condition",
            "Cluster_Name",
            "Next_Condition"
        ]

        columns = [col for col in columns if col in child_records[0]]

        self.table.setColumnCount(len(columns))
        self.table.setRowCount(len(child_records))
        self.table.setHorizontalHeaderLabels(columns)

        for row_idx, record in enumerate(child_records):
            for col_idx, col in enumerate(columns):
                item = QTableWidgetItem(str(record.get(col, "")))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row_idx, col_idx, item)

        self.table.resizeColumnsToContents()