# controller/hash_controller.py
from PyQt5.QtCore import QTimer
import pyperclip

from model.hash_model import HashModel


class HashController:

    def __init__(self, view):
        self.view = view
        self.model = HashModel()

        self.hash_chars = []
        self.index = 0

        self._connect_events()
        self._load_algorithms()

    # -------------------------------------------------------
    # SETUP
    # -------------------------------------------------------
    def _connect_events(self):
        ui = self.view.ui

        ui.generatehash.clicked.connect(self.on_generate)
        ui.selectfile.clicked.connect(self.on_pick_file)
        ui.help_btn.clicked.connect(self.view.show_help)
        ui.copyhash.clicked.connect(self.on_copy)
        ui.pasttext.clicked.connect(self.on_paste)

        # timer for animation
        self.view.timer.timeout.connect(self._animate_step)

    def _load_algorithms(self):
        algos = self.model.get_algorithms()
        self.view.populate_algorithms(algos)

    # -------------------------------------------------------
    # USER ACTIONS
    # -------------------------------------------------------
    def on_paste(self):
        try:
            self.view.set_text_input(pyperclip.paste())
        except Exception:
            pass

    def on_copy(self):
        try:
            pyperclip.copy(self.view.ui.yourhash.toPlainText())
            self.view.show_info("Copy Hash", "Hash copied to clipboard.")
        except Exception as e:
            self.view.show_error("Clipboard Error", str(e))

    def on_pick_file(self):
        path = self.view.ask_file()
        if not path:
            return
        try:
            content = self.model.read_file(path)
            self.view.set_text_input(content)
        except Exception as e:
            self.view.show_error("File Error", str(e))

    # -------------------------------------------------------
    # HASH GENERATION
    # -------------------------------------------------------
    def on_generate(self):
        txt = self.view.get_text_input()
        if not txt:
            self.view.show_error("Input Error", "Please enter text.")
            return

        alg = self.view.get_algorithm()
        try:
            hex_hash = self.model.compute_hash(txt, alg)
        except ValueError:
            self.view.show_error("Algorithm Error", f"Unsupported: {alg}")
            return
        except Exception as e:
            self.view.show_error("Hash Error", str(e))
            return

        self._prepare_animation(hex_hash)

    # -------------------------------------------------------
    # ANIMATION
    # -------------------------------------------------------
    def _prepare_animation(self, hex_hash):
        self.hash_chars = list(hex_hash)
        self.index = 0

        self.view.clear_hash_result()
        self.view.disable_inputs()

        interval = max(8, min(40, int(400 / max(1, len(self.hash_chars)))))
        self.view.timer.start(interval)

    def _animate_step(self):
        if self.index < len(self.hash_chars):
            old = self.view.ui.yourhash.toPlainText()
            self.view.set_hash_result(old + self.hash_chars[self.index])

            progress = int((self.index + 1) * 100 / len(self.hash_chars))
            self.view.ui.progressBar.setValue(progress)

            self.index += 1
        else:
            self.view.timer.stop()
            self.view.show_complete()
            self.view.enable_inputs()
