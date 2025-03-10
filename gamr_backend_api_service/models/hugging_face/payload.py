import base64
from pathlib import Path
from typing import Self

import numpy as np
from fastapi import Response
from pydantic import BaseModel, Field, model_validator

ALLOWED_EXTENSIONS = [".png", ".jpg", ".jpeg"]


class ImagePayload(BaseModel):
    filename: str = Field(min_length=1)
    image_bytes: bytes
    model_service: str

    @model_validator(mode="after")
    def validate_filename(self) -> Self:
        if Path(self.filename).suffix.lower() not in ALLOWED_EXTENSIONS:
            msg = "Wrong filename format"
            raise ValueError(msg)

        return self

    @property
    def list_encoded_image(self) -> list[int]:
        image_bytes_decoded = base64.b64decode(self.image_bytes)
        image_list: list[int] = np.frombuffer(
            image_bytes_decoded, dtype=np.uint8
        ).tolist()
        return image_list

    @property
    def response(self) -> Response:
        return Response(content=self.image_bytes, media_type="image/png")
