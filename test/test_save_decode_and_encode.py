import os
import unittest
from typing import Final

from sinisistar2save import SiNiSiStar2Save

SAVE_FOLDER: Final[str] = os.path.join(
    os.getenv("USERPROFILE", os.path.expanduser("~")),
    "AppData", "LocalLow", "Uu", "SiNiSistar2", "SaveData"
)
TARGET_SAVE_FILE: Final[str] = os.path.join(SAVE_FOLDER, "FileAuto")


class SaveDecodeAndEncode(unittest.TestCase):
    def test_save_decode_and_encode(self):
        with open(TARGET_SAVE_FILE, 'r', encoding="utf-8-sig") as file:
            data = file.read()
        save = SiNiSiStar2Save.parse(data)
        re_encoded = save.encode()
        re_decoded = SiNiSiStar2Save.parse(re_encoded)

        self.assertEqual(save.data, re_decoded.data)
        self.assertEqual(save.image, re_decoded.image)
