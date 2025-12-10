# main.py
import sys
from PyQt5.QtWidgets import QApplication

from view.main_window import HashView
from controller.hash_controller import HashController


def main():
    app = QApplication(sys.argv)

    view = HashView()
    controller = HashController(view)

    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
