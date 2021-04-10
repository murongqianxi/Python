# --省略-- #

class Window(QMainWindow):
    """主窗口"""

    def __init__(self, parent=None):
        """设置窗口内容"""
        # --省略--
        self._connectSlot()

    # --省略--

    def _connectSlot(self):
        '''设置每个菜单项的操作，使用lambda创建匿名函数是为了节省代码'''
        self.quitAction.triggered.connect(lambda: sys.exit())


# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
