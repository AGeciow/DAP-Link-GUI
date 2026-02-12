from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit, QComboBox, QLabel
)
from backend.pyocd_backend import PyOCDBackend

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.backend = PyOCDBackend()

		self.setWindowTitle("DAP Programmer")
		self.resize(500, 300)

		self.log = QTextEdit()
		self.log.setReadOnly(True)

		self.devices = QComboBox()
		#self.refresh_devices()

		self.flash_btn = QPushButton("Flash")
		self.flash_btn.clicked.connect(self.flash)
		
		self.erase_btn = QPushButton("Erase")
		self.erase_btn.clicked.connect(self.erase)
		
		self.refresh_btn = QPushButton("Refresh Devices")
		self.refresh_btn.clicked.connect(self.refresh_devices)

		layout = QVBoxLayout()
		layout.addWidget(QLabel("Devices"))
		layout.addWidget(self.devices)
		layout.addWidget(self.refresh_btn)
		layout.addWidget(self.flash_btn)
		layout.addWidget(self.erase_btn)
		layout.addWidget(self.log)

		container = QWidget()
		container.setLayout(layout)
		self.setCentralWidget(container)

	def refresh_devices(self):
		self.devices.clear()
		for p in self.backend.list_probes():
			self.devices.addItem(p)

	def flash(self):
		fw, _ = QFileDialog.getOpenFileName(self, "Select firmware")
		if not fw:
			return

		uid = self.devices.currentText()
		try:
			self.backend.connect(uid)
			self.backend.flash(fw)
			self.backend.reset()
			self.backend.disconnect()

			self.log.append(f"✔ Flash OK: {fw}")

		except Exception as e:
			self.log.append(f"❌ {e}")


	def erase(self):
		uid = self.devices.currentText()

		try:
			self.backend.connect(uid)
			self.backend.erase()
			self.backend.disconnect()

			self.log.append("✔ Chip erased")

		except Exception as e:
			self.log.append(f"❌ {e}")

