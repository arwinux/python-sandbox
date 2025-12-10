# view/main_window.py
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5 import QtGui
import pyperclip

from .HashGenerator import Ui_MainWindow_HashGenerator


class HashView(QMainWindow):
    """Pure UI layer. Emits actions & displays results."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_HashGenerator()
        self.ui.setupUi(self)

        self.old_pos = QPoint()
        self.timer = QTimer(self)
        self.timer.stop()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self._setup_progressbar()
        self._connect_static_ui()

    # -------------------------------------------------------
    # INITIAL SETUP
    # -------------------------------------------------------
    def populate_algorithms(self, algorithms: list):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(algorithms)

    def _setup_progressbar(self):
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setTextVisible(False)

    def _connect_static_ui(self):
        # Only UI events here — controller will attach actions
        self.ui.copyhash.setEnabled(False)

    # -------------------------------------------------------
    # WINDOW DRAG
    # -------------------------------------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    # -------------------------------------------------------
    # SIMPLE VIEW HELPERS
    # -------------------------------------------------------
    def show_error(self, title, msg):
        QMessageBox.critical(self, title, msg)

    def show_info(self, title, msg):
        QMessageBox.information(self, title, msg)

    def get_text_input(self):
        return self.ui.yourtext.toPlainText()

    def set_text_input(self, txt):
        self.ui.yourtext.setPlainText(txt)

    def set_hash_result(self, txt):
        self.ui.yourhash.setPlainText(txt)

    def clear_hash_result(self):
        self.ui.yourhash.clear()
        self.ui.complete.setText("")
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setTextVisible(True)
        self.ui.copyhash.setEnabled(False)

    def show_complete(self):
        self.ui.complete.setText("Complete ...")
        self.ui.progressBar.setTextVisible(False)
        self.ui.copyhash.setEnabled(True)

    def get_algorithm(self):
        return self.ui.comboBox.currentText().strip()

    def disable_inputs(self):
        self.ui.generatehash.setEnabled(False)
        self.ui.selectfile.setEnabled(False)
        self.ui.pasttext.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.copyhash.setEnabled(False)

    def enable_inputs(self):
        self.ui.generatehash.setEnabled(True)
        self.ui.selectfile.setEnabled(True)
        self.ui.pasttext.setEnabled(True)
        self.ui.comboBox.setEnabled(True)

    # -------------------------------------------------------
    # FILE PICKER
    # -------------------------------------------------------
    def ask_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File")
        return path or None

    # -------------------------------------------------------
    # HELP DIALOG
    # -------------------------------------------------------
    def show_help(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Developer Information")
        msg.setIcon(QMessageBox.Information)

        try:
            msg.setWindowIcon(QtGui.QIcon("assets/royal_lionn.ico"))
        except Exception:
            pass

        msg.setText(
            "Developer: Arvin Jafary\n"
            "-------------------------------\n"
            "Email: arwinux@gmail.com"
        )
        msg.exec_()
