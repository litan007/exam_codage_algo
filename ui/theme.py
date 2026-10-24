"""
Thème visuel et générateur d'icônes vectorielles modernes pour NovaZip Pro.
Offre une interface de bureau Windows native, professionnelle et élégante (Thème Émeraude & Slate).
"""

from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QBrush, QFont, QPolygon
from PySide6.QtCore import Qt, QPoint, QRectF


class WinRARTheme:
    """Palette de couleurs et feuille de style QSS moderne (NovaZip Pro)."""

    QSS_STYLESHEET = """
    QWidget {
        color: #0F172A;
    }
    QMainWindow, QDialog {
        background-color: #F8FAFC;
        color: #0F172A;
    }
    QMenuBar {
        background-color: #F1F5F9;
        border-bottom: 1px solid #E2E8F0;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
        padding: 2px;
        color: #0F172A;
    }
    QMenuBar::item {
        background-color: transparent;
        padding: 5px 12px;
        border-radius: 4px;
        color: #0F172A;
    }
    QMenuBar::item:selected {
        background-color: #E2E8F0;
        color: #0F766E;
    }
    QMenu {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
        padding: 4px;
        color: #0F172A;
        border-radius: 4px;
    }
    QMenu::item {
        padding: 6px 24px 6px 20px;
        border-radius: 3px;
        color: #0F172A;
    }
    QMenu::item:selected {
        background-color: #F0FDFA;
        color: #0F766E;
    }
    QMenu::separator {
        height: 1px;
        background-color: #E2E8F0;
        margin: 4px 8px;
    }
    QToolBar {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #F8FAFC);
        border-top: 1px solid #FFFFFF;
        border-bottom: 1px solid #E2E8F0;
        spacing: 6px;
        padding: 4px 8px;
    }
    QToolButton {
        background-color: transparent;
        border: 1px solid transparent;
        border-radius: 4px;
        padding: 4px 10px;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 11px;
        font-weight: 600;
        color: #1E293B;
    }
    QToolButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #F0FDFA, stop:1 #CCFBF1);
        border: 1px solid #5EEAD4;
        color: #0F766E;
    }
    QToolButton:pressed {
        background: #99F6E4;
        border: 1px solid #14B8A6;
    }
    QLineEdit {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        padding: 4px 8px;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
        color: #0F172A;
    }
    QLineEdit:focus {
        border: 1px solid #0D9488;
    }
    QTableWidget, QTableView {
        background-color: #FFFFFF;
        alternate-background-color: #F8FAFC;
        color: #0F172A;
        border: 1px solid #E2E8F0;
        gridline-color: #F1F5F9;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
        selection-background-color: #CCFBF1;
        selection-color: #0F766E;
    }
    QTableWidget::item, QTableView::item {
        color: #0F172A;
        background-color: transparent;
        padding: 5px 8px;
    }
    QTableWidget::item:selected, QTableView::item:selected {
        background-color: #CCFBF1;
        color: #0F766E;
        font-weight: 600;
    }
    QHeaderView::section {
        background-color: #F1F5F9;
        color: #0F172A;
        font-weight: 700;
        font-size: 11px;
        padding: 6px 8px;
        border: none;
        border-right: 1px solid #E2E8F0;
        border-bottom: 2px solid #0D9488;
    }
    QTableCornerButton::section {
        background-color: #F1F5F9;
        border: 1px solid #E2E8F0;
    }
    QComboBox {
        background-color: #FFFFFF;
        color: #0F172A;
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        padding: 4px 8px;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
    }
    QComboBox:focus {
        border: 1px solid #0D9488;
    }
    QComboBox QAbstractItemView {
        background-color: #FFFFFF;
        color: #0F172A;
        selection-background-color: #CCFBF1;
        selection-color: #0F766E;
        border: 1px solid #CBD5E1;
    }
    QTextEdit, QPlainTextEdit {
        background-color: #FFFFFF;
        color: #0F172A;
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        font-family: "Segoe UI", Arial, sans-serif;
    }
    QLabel {
        color: #0F172A;
    }
    QStatusBar {
        background-color: #F1F5F9;
        border-top: 1px solid #E2E8F0;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 11px;
        color: #1E293B;
    }
    QStatusBar::item {
        border: 1px solid #E2E8F0;
        border-radius: 3px;
        padding: 2px 8px;
        background-color: #FFFFFF;
        color: #0F172A;
    }
    QProgressBar {
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        background-color: #E2E8F0;
        text-align: center;
        font-weight: 600;
        font-size: 11px;
        color: #0F172A;
    }
    QProgressBar::chunk {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0D9488, stop:1 #06B6D4);
        border-radius: 3px;
    }
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #F8FAFC);
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        padding: 5px 16px;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
        color: #0F172A;
        min-width: 75px;
    }
    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #F0FDFA, stop:1 #CCFBF1);
        border: 1px solid #0D9488;
        color: #0F766E;
    }
    QPushButton:pressed {
        background: #99F6E4;
        border: 1px solid #0F766E;
    }
    QPushButton:default {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0D9488, stop:1 #0F766E);
        border: 1px solid #0F766E;
        color: #FFFFFF;
        font-weight: 700;
    }
    QPushButton:default:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #14B8A6, stop:1 #0D9488);
        color: #FFFFFF;
    }
    QGroupBox {
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
        font-weight: 600;
        color: #0F172A;
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        margin-top: 12px;
        padding-top: 12px;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        left: 10px;
        padding: 0 4px;
        background-color: #F8FAFC;
        color: #0F766E;
    }
    QTabWidget::pane {
        border: 1px solid #CBD5E1;
        background-color: #FFFFFF;
        border-radius: 4px;
    }
    QTabBar::tab {
        background-color: #E2E8F0;
        color: #334155;
        padding: 6px 16px;
        border: 1px solid #CBD5E1;
        border-bottom: none;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        font-family: "Segoe UI", Arial, sans-serif;
        font-size: 12px;
    }
    QTabBar::tab:selected {
        background-color: #FFFFFF;
        color: #0F766E;
        font-weight: 700;
    }
    """

    @staticmethod
    def create_table_item(
        text: str,
        align=Qt.AlignLeft | Qt.AlignVCenter,
        fg_color: str = "#0F172A",
        bold: bool = False,
        icon: QIcon = None,
        font_family: str = "Segoe UI",
        font_size: int = 9,
    ):
        from PySide6.QtWidgets import QTableWidgetItem
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(align)
        item.setForeground(QColor(fg_color))
        font = QFont(font_family, font_size)
        if bold:
            font.setBold(True)
        item.setFont(font)
        if icon:
            item.setIcon(icon)
        return item

    @staticmethod
    def create_vector_icon(icon_type: str, size: int = 32) -> QIcon:
        """
        Génère une icône vectorielle moderne et nette pour NovaZip Pro.
        """
        pix = QPixmap(size, size)
        pix.fill(Qt.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)

        s = float(size)

        if icon_type == "add":
            # Coffre d'archive moderne avec insigne Plus vert émeraude
            p.setPen(QPen(QColor("#0F766E"), 1.2))
            p.setBrush(QBrush(QColor("#14B8A6")))
            p.drawRoundedRect(QRectF(s * 0.15, s * 0.30, s * 0.55, s * 0.52), 4, 4)

            # Couvercle de boîte
            p.setBrush(QBrush(QColor("#0D9488")))
            p.drawRoundedRect(QRectF(s * 0.12, s * 0.22, s * 0.61, s * 0.14), 2, 2)

            # Insigne PLUS vert émeraude en bas à droite
            p.setPen(QPen(QColor("#065F46"), 1.2))
            p.setBrush(QBrush(QColor("#10B981")))
            p.drawEllipse(QRectF(s * 0.52, s * 0.52, s * 0.42, s * 0.42))
            p.setPen(QPen(Qt.white, 2.5))
            p.drawLine(QPoint(int(s * 0.73), int(s * 0.60)), QPoint(int(s * 0.73), int(s * 0.86)))
            p.drawLine(QPoint(int(s * 0.60), int(s * 0.73)), QPoint(int(s * 0.86), int(s * 0.73)))

        elif icon_type == "extract":
            # Coffre d'archive ouvert avec flèche d'extraction cyan vers le haut
            p.setPen(QPen(QColor("#0F766E"), 1.2))
            p.setBrush(QBrush(QColor("#14B8A6")))
            p.drawRoundedRect(QRectF(s * 0.15, s * 0.45, s * 0.55, s * 0.40), 4, 4)

            # Flèche montante cyan dynamique
            p.setPen(QPen(QColor("#0284C7"), 1.2))
            p.setBrush(QBrush(QColor("#0EA5E9")))
            poly = QPolygon([
                QPoint(int(s * 0.55), int(s * 0.38)),
                QPoint(int(s * 0.85), int(s * 0.12)),
                QPoint(int(s * 0.68), int(s * 0.12)),
                QPoint(int(s * 0.85), int(s * 0.12)),
                QPoint(int(s * 0.85), int(s * 0.29)),
            ])
            p.drawPolygon(poly)
            p.setPen(QPen(QColor("#0284C7"), 3.2))
            p.drawLine(QPoint(int(s * 0.42), int(s * 0.52)), QPoint(int(s * 0.80), int(s * 0.16)))

        elif icon_type == "test":
            # Bouclier de sécurité émeraude avec coche blanche
            p.setPen(QPen(QColor("#065F46"), 1.5))
            p.setBrush(QBrush(QColor("#10B981")))
            shield = QPolygon([
                QPoint(int(s * 0.50), int(s * 0.12)),
                QPoint(int(s * 0.82), int(s * 0.22)),
                QPoint(int(s * 0.82), int(s * 0.55)),
                QPoint(int(s * 0.50), int(s * 0.88)),
                QPoint(int(s * 0.18), int(s * 0.55)),
                QPoint(int(s * 0.18), int(s * 0.22)),
            ])
            p.drawPolygon(shield)

            # Coche blanche nette
            p.setPen(QPen(Qt.white, 2.8))
            p.drawLine(QPoint(int(s * 0.35), int(s * 0.50)), QPoint(int(s * 0.46), int(s * 0.65)))
            p.drawLine(QPoint(int(s * 0.46), int(s * 0.65)), QPoint(int(s * 0.68), int(s * 0.38)))

        elif icon_type == "view":
            # Document avec loupe d'inspection
            p.setPen(QPen(QColor("#0D9488"), 3.0))
            p.setBrush(QBrush(QColor(240, 253, 250, 200)))
            p.drawEllipse(QRectF(s * 0.18, s * 0.18, s * 0.45, s * 0.45))
            p.setPen(QPen(QColor("#1E293B"), 3.5))
            p.drawLine(QPoint(int(s * 0.52), int(s * 0.52)), QPoint(int(s * 0.82), int(s * 0.82)))

        elif icon_type == "delete":
            # Corbeille / croix rouge vif moderne
            p.setPen(QPen(QColor("#B91C1C"), 1.2))
            p.setBrush(QBrush(QColor("#EF4444")))
            p.drawRoundedRect(QRectF(s * 0.22, s * 0.30, s * 0.56, s * 0.55), 3, 3)

            # Couvercle
            p.setBrush(QBrush(QColor("#DC2626")))
            p.drawRoundedRect(QRectF(s * 0.16, s * 0.20, s * 0.68, s * 0.12), 2, 2)
            p.drawRect(QRectF(s * 0.40, s * 0.14, s * 0.20, s * 0.08))

            # Rayures corbeille
            p.setPen(QPen(Qt.white, 1.8))
            p.drawLine(QPoint(int(s * 0.36), int(s * 0.40)), QPoint(int(s * 0.36), int(s * 0.75)))
            p.drawLine(QPoint(int(s * 0.50), int(s * 0.40)), QPoint(int(s * 0.50), int(s * 0.75)))
            p.drawLine(QPoint(int(s * 0.64), int(s * 0.40)), QPoint(int(s * 0.64), int(s * 0.75)))

        elif icon_type == "info":
            # Badge circulaire émeraude 'i'
            p.setPen(QPen(QColor("#0F766E"), 1.2))
            p.setBrush(QBrush(QColor("#0D9488")))
            p.drawEllipse(QRectF(s * 0.15, s * 0.15, s * 0.70, s * 0.70))
            p.setPen(QPen(Qt.white, 3.0))
            p.drawPoint(QPoint(int(s * 0.50), int(s * 0.36)))
            p.drawLine(QPoint(int(s * 0.50), int(s * 0.48)), QPoint(int(s * 0.50), int(s * 0.68)))

        elif icon_type == "search":
            # Loupe de recherche saphir/cyan
            p.setPen(QPen(QColor("#0284C7"), 2.8))
            p.setBrush(QBrush(QColor(224, 242, 254, 180)))
            p.drawEllipse(QRectF(s * 0.18, s * 0.18, s * 0.46, s * 0.46))
            p.setPen(QPen(QColor("#0369A1"), 3.5))
            p.drawLine(QPoint(int(s * 0.53), int(s * 0.53)), QPoint(int(s * 0.82), int(s * 0.82)))

        elif icon_type == "folder":
            # Dossier ambre chaleureux
            p.setPen(QPen(QColor("#D97706"), 1.0))
            p.setBrush(QBrush(QColor("#F59E0B")))
            p.drawRoundedRect(QRectF(s * 0.10, s * 0.30, s * 0.80, s * 0.55), 3, 3)
            p.setBrush(QBrush(QColor("#FCD34D")))
            p.drawRoundedRect(QRectF(s * 0.10, s * 0.20, s * 0.35, s * 0.18), 2, 2)

        elif icon_type == "archive":
            # Icône signature NovaZip : Coffre archive sécurisé avec fermoir métallique doré
            p.setPen(QPen(QColor("#0F766E"), 1.2))
            p.setBrush(QBrush(QColor("#0D9488")))
            p.drawRoundedRect(QRectF(s * 0.14, s * 0.24, s * 0.72, s * 0.62), 4, 4)

            # Bandeau de fermeture
            p.setBrush(QBrush(QColor("#14B8A6")))
            p.drawRect(QRectF(s * 0.14, s * 0.46, s * 0.72, s * 0.18))

            # Boucle dorée / fermoir
            p.setPen(QPen(QColor("#B45309"), 1.2))
            p.setBrush(QBrush(QColor("#F59E0B")))
            p.drawRoundedRect(QRectF(s * 0.40, s * 0.42, s * 0.20, s * 0.26), 2, 2)
            p.setBrush(QBrush(QColor("#FEF3C7")))
            p.drawRect(QRectF(s * 0.46, s * 0.49, s * 0.08, s * 0.12))

        elif icon_type == "file":
            # Feuille blanche avec coin replié
            p.setPen(QPen(QColor("#94A3B8"), 1.0))
            p.setBrush(QBrush(Qt.white))
            poly = QPolygon([
                QPoint(int(s * 0.20), int(s * 0.15)),
                QPoint(int(s * 0.60), int(s * 0.15)),
                QPoint(int(s * 0.80), int(s * 0.35)),
                QPoint(int(s * 0.80), int(s * 0.85)),
                QPoint(int(s * 0.20), int(s * 0.85)),
            ])
            p.drawPolygon(poly)
            p.setPen(QPen(QColor("#CBD5E1"), 1.0))
            p.drawLine(QPoint(int(s * 0.30), int(s * 0.45)), QPoint(int(s * 0.70), int(s * 0.45)))
            p.drawLine(QPoint(int(s * 0.30), int(s * 0.55)), QPoint(int(s * 0.70), int(s * 0.55)))
            p.drawLine(QPoint(int(s * 0.30), int(s * 0.65)), QPoint(int(s * 0.60), int(s * 0.65)))

        elif icon_type == "demo":
            # Symbole fonctionnel analytique
            p.setPen(QPen(QColor("#0D9488"), 1.2))
            p.setBrush(QBrush(QColor("#F0FDFA")))
            p.drawRoundedRect(QRectF(s * 0.15, s * 0.15, s * 0.70, s * 0.70), 4, 4)
            p.setPen(QPen(QColor("#0F766E"), 2.0))
            p.setFont(QFont("Segoe UI", int(s * 0.38), QFont.Bold))
            p.drawText(QRectF(0, 0, s, s), Qt.AlignCenter, "f(x)")

        elif icon_type == "benchmark":
            # Tachymètre / vitesse
            p.setPen(QPen(QColor("#0D9488"), 2.0))
            p.setBrush(QBrush(QColor("#F0FDFA")))
            p.drawPie(QRectF(s * 0.15, s * 0.20, s * 0.70, s * 0.70), 0, 180 * 16)
            p.setPen(QPen(QColor("#0F766E"), 2.5))
            p.drawLine(QPoint(int(s * 0.50), int(s * 0.55)), QPoint(int(s * 0.70), int(s * 0.35)))

        p.end()
        return QIcon(pix)
