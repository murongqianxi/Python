# -*- coding: utf-8 -*-
# @Time : 2022/2/9 15:30
# @Author : Liu Mingshuai
# @File : 01

# 1
import sys

from PySide6.QtWidgets import QApplication, QLabel

# 2
app = QApplication(sys.argv)
label = QLabel('Hello World!')
# 3
label.show()
# 4
sys.exit(app.exec())
