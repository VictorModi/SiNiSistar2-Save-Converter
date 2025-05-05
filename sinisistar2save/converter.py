import base64
import json
from dataclasses import dataclass
from typing import Dict, Optional, Any


@dataclass
class SiNiSiStar2Save:
    data: Dict[str, Any]
    image: Optional[bytes]

    @staticmethod
    def parse(data: str) -> "SiNiSiStar2Save":
        data_lines: list[str] = data.splitlines()  # 0 for game data, 1 for image (png)
        decoded_data: str = base64.b64decode(data_lines[0])[::-1].decode("utf-8", "ignore")
        parsed_data: Dict[str, Any] = json.loads(decoded_data)
        image_data: Optional[bytes] = base64.b64decode(data_lines[1]) if len(data_lines) > 1 else None
        return SiNiSiStar2Save(parsed_data, image_data)

    def encode(self) -> str:
        reversed_data: bytes = json.dumps(self.data, indent=4).encode("utf-8")[::-1]
        encoded_data: str = base64.b64encode(reversed_data).decode("utf-8")
        if self.image is not None:
            encoded_image: str = base64.b64encode(self.image).decode("utf-8")
            return f"{encoded_data}\n{encoded_image}"
        return encoded_data
