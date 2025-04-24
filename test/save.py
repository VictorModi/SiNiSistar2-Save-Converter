import os
import unittest
from typing import Final

from sinisistar2save.converter import SiNiSiStar2Save

SAVE_FOLDER: Final[str] = f"C:\\Users\\{os.getlogin()}\\AppData\\LocalLow\\Uu\\SiNiSistar2\\SaveData"


class SaveDecodeTest(unittest.TestCase):
    def test_save_decode(self):
        test_save_file_name: Final[str] = f"{SAVE_FOLDER}\\FileAuto"
        with open(test_save_file_name, 'r', encoding="utf-8-sig") as file:
            data = file.read()
        save = SiNiSiStar2Save.parse(data)
        print(save)
        self.assertIsNotNone(save)
        self.assertIsInstance(save.data, dict)
        self.assertIsInstance(save.image, (bytes, type(None)))
