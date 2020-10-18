from translator import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QGraphicsDropShadowEffect, QMenu
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'papago translator'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 200
        self.opacity = 100
        self.font_size = 13
        self.x = None
        self.y = None
        self.th = None
        self.label = None
        self.opacity_slider = None
        self.text_size_slider = None
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.set_opacity_slider()
        self.set_text_size_slider()
        self.set_label()
        self.initialize_thread()
        self.show()

    def set_opacity_slider(self):
        self.opacity_slider = QSlider(Qt.Vertical, self)
        self.opacity_slider.setGeometry(10, 10, 10, 180)
        self.opacity_slider.setMaximum(230)
        self.opacity_slider.setMinimum(30)
        self.opacity_slider.setSliderPosition(127)
        self.opacity_slider.valueChanged[int].connect(self.change_opacity)

    def set_text_size_slider(self):
        self.text_size_slider = QSlider(Qt.Vertical, self)
        self.text_size_slider.setGeometry(20, 10, 10, 180)
        self.text_size_slider.setMaximum(30)
        self.text_size_slider.setMinimum(4)
        self.text_size_slider.setSliderPosition(13)
        self.text_size_slider.valueChanged[int].connect(self.update_font_size)

    def set_label(self):
        self.label = QLabel('', self)
        self.label.setWordWrap(True)
        self.label.setGeometry(40, 30, 770, 200)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.update_font_size(self.font_size)
        font_effect = QGraphicsDropShadowEffect()
        font_effect.setOffset(0,0)
        font_effect.setBlurRadius(10)
        font_effect.setColor(QColor(255, 255, 255))
        self.label.setGraphicsEffect(font_effect)

    def initialize_thread(self):
        self.th = Thread()
        self.th.threadEvent.connect(self.refresh)
        self.th.start()

    def change_opacity(self, value):
        self.opacity = value
        self.update()

    def update_font_size(self, value):
        self.font_size = value
        font = self.font()
        font.setPointSize(self.font_size)
        font.setBold(True)
        self.label.setFont(font)

    def refresh(self):
        if self.th.is_updated():
            self.label.setText(self.th.get_translate())

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def mouseMoveEvent(self, event):
        self.move(event.globalX() - self.x, event.globalY() - self.y)

    def paintEvent(self, event):
        backgroundcolor = QColor(230, 230, 230)
        backgroundcolor.setAlpha(self.opacity)
        backgroundPainter = QPainter(self)
        backgroundPainter.fillRect(QRect(0, 0, self.width, self.height), backgroundcolor)

    def contextMenuEvent(self, QContextMenuEvent):
        menu = QMenu(self)
        quit_action = menu.addAction("quit")
        if self.th.get_lang() == "en":
            lang_action = menu.addAction("jp")
        else:
            lang_action = menu.addAction("en")
        action = menu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit_action:
            self.close()
        elif action == lang_action:
            self.th.change_lang()
            self.label.setText(self.th.get_translate())

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    app.exec_()
