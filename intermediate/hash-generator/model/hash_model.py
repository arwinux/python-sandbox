# model/hash_model.py
import hashlib
from pathlib import Path


class HashModel:
    """Pure logic: algorithms, hashing, file reading."""

    UNWANTED = {
        "md4", "md5", "sm3", "mdc2", "sha1",
        "blake2b", "blake2s", "whirlpool",
        "ripemd160", "shake_128"
    }

    @staticmethod
    def get_algorithms():
        """Return a clean list of allowed hash algorithms."""
        available = set(hashlib.algorithms_available)
        
        safe_algos = sorted(a for a in available if a not in HashModel.UNWANTED)
        return safe_algos or ["sha256"]

    @staticmethod
    def compute_hash(text: str, algorithm: str):
        """Compute hash safely, raising ValueError if unsupported."""
        h = hashlib.new(algorithm)
        h.update(text.encode("utf-8"))
        return h.hexdigest()

    @staticmethod
    def read_file(path: str):
        """Read file as UTF-8 (fallback with replacement)."""
        p = Path(path)
        if not p.exists() or not p.is_file():
            raise FileNotFoundError("Selected path is not a valid file")

        try:
            return p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return p.read_text(encoding="utf-8", errors="replace")
