import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap


class Window(QMainWindow):
    """主窗口"""

    def __init__(self, parent=None):
        """设置窗口内容"""
        super().__init__(parent)
        self.setWindowTitle("笑笑陪你😁")
        self.resize(280, 230)
        self.pixmap = QPixmap('robot.png')
        self.mylabel = QLabel('请选择菜单')
        self.mylabel.setWordWrap(True)
        self.mylabel.setPixmap(self.pixmap)
        self.centralWidget = self.mylabel
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
