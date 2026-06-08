from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QGridLayout
)
from PySide6.QtCore import Qt


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Hero Section
        hero = QFrame()
        hero.setStyleSheet("""
            QFrame{
                background:#DFF3FF;
                border-radius:25px;
                border:2px solid #BDEBFF;
            }
        """)

        hero_layout = QHBoxLayout(hero)

        left = QVBoxLayout()

        title = QLabel("🧸 Child Malnutrition Monitoring System")
        title.setStyleSheet("""
            font-size:32px;
            font-weight:800;
            color:#0D47A1;
        """)

        subtitle = QLabel(
            "A child-friendly machine learning system for nutrition monitoring, "
            "trend analysis and future condition prediction."
        )
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("""
            font-size:16px;
            color:#456A7A;
        """)

        left.addWidget(title)
        left.addWidget(subtitle)

        icon = QLabel("👶 🥣 📈")
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet("font-size:60px;")

        hero_layout.addLayout(left, 3)
        hero_layout.addWidget(icon, 1)

        main_layout.addWidget(hero)

        # Cards
        grid = QGridLayout()
        grid.setSpacing(18)

        cards = [
            ("👶", "Total Children", "3041", "#FFF8E1", "#F9A825"),
            ("📋", "Visit Records", "6785", "#EDE7F6", "#7E57C2"),
            ("📈", "Improved", "717", "#E8F5E9", "#43A047"),
            ("⚠️", "Deteriorated", "349", "#FFF3E0", "#FB8C00"),
            ("💙", "Stable", "270", "#E0F7FA", "#00ACC1"),
            ("🤖", "Accuracy", "73.65%", "#FCE4EC", "#EC407A")
        ]

        for i, (icon, title, value, bg, color) in enumerate(cards):
            card = self.create_card(icon, title, value, bg, color)
            grid.addWidget(card, i // 3, i % 3)

        main_layout.addLayout(grid)

        # Footer Note
        note = QLabel(
            "🌟 This dashboard summarizes child nutrition records, trend findings and machine learning prediction performance."
        )
        note.setWordWrap(True)
        note.setStyleSheet("""
            background:#FFF8E1;
            padding:14px;
            border-radius:14px;
            font-size:15px;
            color:#4E6570;
        """)

        main_layout.addWidget(note)

    def create_card(self, icon, title, value, bg_color, accent_color):

        card = QFrame()

        card.setStyleSheet(f"""
            QFrame {{
                background:{bg_color};
                border-radius:22px;
                border:none;
            }}
        """)

        layout = QVBoxLayout(card)

        icon_label = QLabel(icon)
        icon_label.setStyleSheet("""
            font-size:34px;
            background:transparent;
        """)

        value_label = QLabel(value)
        value_label.setStyleSheet(f"""
            font-size:34px;
            font-weight:900;
            color:{accent_color};
            background:transparent;
        """)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size:16px;
            font-weight:700;
            color:#355869;
            background:transparent;
        """)

        layout.addWidget(icon_label)
        layout.addWidget(value_label)
        layout.addWidget(title_label)

        return card