from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QListWidget, QStackedWidget
)
from PySide6.QtCore import QSize

from ui.dashboard_page import DashboardPage
from ui.child_history_page import ChildHistoryPage
from ui.prediction_page import PredictionPage
from ui.analytics_page import AnalyticsPage
from ui.about_page import AboutPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Child Malnutrition Monitoring System")

        # Better window size
        self.setMinimumSize(1200, 750)
        self.resize(1350, 820)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5FBFF;
            }

            QWidget {
                background-color: #F5FBFF;
            }

            QListWidget {
                background-color: #E3F2FD;
                border: 2px solid #B3E5FC;
                border-radius: 20px;
                padding: 10px;
                font-size: 15px;
                color: #174A63;
                font-weight: 600;
                outline: none;
            }

            QListWidget::item {
                height: 48px;
                padding-left: 12px;
                margin: 5px;
                border-radius: 14px;
            }

            QListWidget::item:selected {
                background-color: #81D4FA;
                color: #003B5C;
            }

            QListWidget::item:hover {
                background-color: #B3E5FC;
            }

            QStackedWidget {
                background-color: #F5FBFF;
                border: none;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(14, 14, 14, 14)
        main_layout.setSpacing(14)

        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(230)
        self.sidebar.setIconSize(QSize(24, 24))

        self.sidebar.addItem("🏠  Dashboard")
        self.sidebar.addItem("🧒  Child History")
        self.sidebar.addItem("🔮  Future Prediction")
        self.sidebar.addItem("📊  Analytics")
        self.sidebar.addItem("🌈  About")

        self.pages = QStackedWidget()
        self.pages.addWidget(DashboardPage())
        self.pages.addWidget(ChildHistoryPage())
        self.pages.addWidget(PredictionPage())
        self.pages.addWidget(AnalyticsPage())
        self.pages.addWidget(AboutPage())

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.pages)

        self.sidebar.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.sidebar.setCurrentRow(0)