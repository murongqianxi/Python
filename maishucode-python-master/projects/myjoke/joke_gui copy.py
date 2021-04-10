import sys

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QAction
from PyQt5.QtGui import QPixmap
import joke_gui_model
import time 
from joke import Joke

class Window(QMainWindow):
    """主窗口"""

    def __init__(self, parent=None):
        """设置窗口内容"""
        # --省略--
        self._connectSlot()

        # 设置后台工作线程
        self.worker = Worker()

        # 当后台发送信号回来，调用_show_joke函数
        self.worker.sinOut.connect(self._show_joke)

        # 当后台进程执行完，调用这个匿名函数，恢复显示图像
        self.worker.finished.connect(
            lambda: self.mylabel.setPixmap(self.pixmap))

    def _addMenu(self):
        # --省略--



    def _createActions(self):
        # --省略--

    def _connectSlot(self):
        '''设置每个菜单项的操作，使用lambda创建匿名函数是为了节省代码'''
        self.quitAction.triggered.connect(lambda : sys.exit())

        # 给每个操作设置关联函数，因为要传入参数，所以使用lambda创建匿名函数，这样可以重用同一个函数
        self.listenAction1.triggered.connect(lambda : self._speak_jokes(1))
        self.listenAction3.triggered.connect(lambda: self._speak_jokes(3))
        self.listenAction5.triggered.connect(lambda: self._speak_jokes(5))
        self.readAction1.triggered.connect(lambda: self._print_jokes(1))
        self.readAction3.triggered.connect(lambda: self._print_jokes(3))
        self.readAction5.triggered.connect(lambda: self._print_jokes(5))

    def _speak_jokes(self, count=1):
        '''启动线程讲笑话，必须启动独立线程，否则会造成窗口卡死不动'''
        # 设置笑话个数
        self.worker.count = count
        # 设置语音，如果是False，则不发音，只是显示笑话
        self.worker.speak_flag = True
        # 启动线程
        self.worker.start()

    def _print_jokes(self, count=1):
        '''启动线程打印笑话，必须启动独立线程，否则会造成窗口卡死不动'''
        self.worker.count = count
        self.worker.speak_flag = False
        self.worker.start()

    def _show_joke(self, joke):
        '''把笑话显示在窗口中'''
        self.mylabel.setText(f'{joke.title} \n {joke.detail}')


class Worker(QThread):
    '''负责朗读笑话和打印笑话的独立线程'''

    # 用来给UI线程发送信息，通过这个变量可以把一个笑话传递给主线程的指定方法
    sinOut = pyqtSignal(Joke)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.count = 1
        # 控制是否要朗读
        self.speak_flag = True 

    def run(self):
        # 获取笑话
        self.jokes = joke_gui_model.select_jokes(self.count)
        for joke in self.jokes:
            self.sinOut.emit(joke)
            if self.speak_flag:
                joke_gui_model.speak_joke(joke)
                # 朗读完成后，短暂停顿0.5秒
                time.sleep(0.5)
            else:
                # 打印完笑话，要停顿2秒，给用户流出时间阅读笑话
                time.sleep(2)
            
# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
