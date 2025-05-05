# SiNiSistar2-Save-Converter

A lightweight Python utility to parse and encode save files from *SiNiSiStar 2*. It decodes the save file into structured JSON data and optionally includes an image section, allowing easy reading and modification.

## Features

- Decode SiNiSistar 2 save files into human-readable format
- Re-encode modified data back into the original save format
- Pure Python, zero dependencies

## Installation

You can install this tool directly via Git:

```bash
pip install git+https://github.com/VictorModi/SiNiSistar2-Save-Converter.git
```

Or clone manually:
```bash
git clone https://github.com/VictorModi/SiNiSistar2-Save-Converter.git
cd SiNiSistar2-Save-Converter
```

## Usage Example
```python
import os

from typing import Final
from sinisistar2save import SiNiSiStar2Save

# Save folder for Windows
SAVE_FOLDER: Final[str] = os.path.join(
    os.getenv("USERPROFILE", os.path.expanduser("~")),
    "AppData", "LocalLow", "Uu", "SiNiSistar2", "SaveData"
)
TARGET_SAVE_FILE: Final[str] = os.path.join(SAVE_FOLDER, "FileAuto")

with open(TARGET_SAVE_FILE, "r", encoding="utf-8-sig") as f:
    raw_data = f.read()
# Parse the save file
save = SiNiSiStar2Save.parse(raw_data)
print(save.data)
save.data["m_StatusSetting"]["m_Relics"] = 114514

# Re-encode and write back to file
with open(TARGET_SAVE_FILE, "w", encoding="utf-8-sig") as f:
    f.write(save.encode())
```

## Notes
 - Encoding: Always open save files using encoding="utf-8-sig" when reading/writing. Example:
```python
with open("path/to/savefile", "r", encoding="utf-8-sig") as f:
    ...
```
 - Image format: If present, the image section must be in **PNG format**. Other formats may cause the game to reject or fail to load the save file.
 - Save File Structure:
    - A base64-encoded, reversed JSON string (line 1)
    - An optional base64-encoded PNG image (line 2)