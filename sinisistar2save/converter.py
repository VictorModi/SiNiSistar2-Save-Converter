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
        data_lines = data.splitlines()
        json_data = json.loads(base64.b64decode(data_lines[0])[::-1].decode("utf-8", "ignore"))
        image_data = base64.b64decode(data_lines[1]) if len(data_lines) > 1 else None
        return SiNiSiStar2Save(json_data, image_data)

    def encode(self) -> str:
        encoded_data = base64.b64encode(
            json.dumps(self.data, indent=4).encode("utf-8")[::-1]
        ).decode("utf-8")
        if self.image is not None:
            encoded_image = base64.b64encode(self.image).decode("utf-8")
            return f"{encoded_data}\n{encoded_image}"
        return encoded_data
