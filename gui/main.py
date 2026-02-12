import sys
from PySide6.QtWidgets import QApplication
from .main_window import MainWindow

def run():
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec())
