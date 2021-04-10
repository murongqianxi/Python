import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QAction, QMenu
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
        self._createActions()
        self._addMenu()
        self._connectSlot()

    def _addMenu(self):
        '''创建菜单，并把_createAction中创建的菜单项添加到菜单下'''
        # QMainWindow默认有一个空白的菜单栏
        menuBar = self.menuBar()
        # 没有这个设置，Mac上不能显示菜单
        menuBar.setNativeMenuBar(False)

        # 添加听笑话菜单和3个菜单项
        listenMenu = QMenu("&听笑话", self)
        listenMenu.addAction(self.listenAction1)
        listenMenu.addAction(self.listenAction3)
        listenMenu.addAction(self.listenAction5)

        # 添加读笑话菜单和3个菜单项
        readMenu = menuBar.addMenu("&读笑话")
        readMenu.addAction(self.readAction1)
        readMenu.addAction(self.readAction3)
        readMenu.addAction(self.readAction5)

        # 添加退出菜单和1个菜单项
        quitMenu = menuBar.addMenu("&退出")
        quitMenu.addAction(self.quitAction)

        # 把3个菜单添加到菜单栏
        menuBar.addMenu(listenMenu)
        menuBar.addMenu(readMenu)
        menuBar.addMenu(quitMenu)

    def _createActions(self):
        '''创建菜单项，这些菜单项被添加到菜单栏'''
        self.readAction1 = QAction("&一个", self)
        self.readAction3 = QAction("&三个", self)
        self.readAction5 = QAction("&五个", self)

        self.listenAction1 = QAction("&一个", self)
        self.listenAction3 = QAction("&三个", self)
        self.listenAction5 = QAction("&五个", self)

        self.quitAction = QAction("&退出", self)

    def _connectSlot(self):
        '''设置每个菜单项的操作，使用lambda创建匿名函数是为了节省代码'''
        self.quitAction.triggered.connect(lambda: sys.exit())


# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
