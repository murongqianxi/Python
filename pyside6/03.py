import sys

from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
qApp.shutdown()
print(app.allWidgets())
