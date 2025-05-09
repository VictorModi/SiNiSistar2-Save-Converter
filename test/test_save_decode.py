import os
import unittest
from typing import Final

from sinisistar2save import SiNiSiStar2Save

SAVE_FOLDER: Final[str] = os.path.join(
    os.getenv("USERPROFILE", os.path.expanduser("~")),
    "AppData", "LocalLow", "Uu", "SiNiSistar2", "SaveData"
)
TARGET_SAVE_FILE: Final[str] = os.path.join(SAVE_FOLDER, "FileAuto")


class SaveDecodeTest(unittest.TestCase):
    def test_save_decode(self):
        with open(TARGET_SAVE_FILE, 'r', encoding="utf-8-sig") as file:
            data = file.read()
        save = SiNiSiStar2Save.parse(data)
        print(save)
        self.assertIsNotNone(save)
        self.assertIsInstance(save.data, dict)
        self.assertIsInstance(save.image, (bytes, type(None)))
