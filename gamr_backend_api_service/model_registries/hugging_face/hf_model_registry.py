import json
from dataclasses import dataclass

from gradio_client import Client

from gamr_backend_api_service.model_registries.abstract_model_registry import (
    AbstractModelRegistry,
)
from gamr_backend_api_service.models import ImageData

from .errors import HuggingFaceException


@dataclass
class HuggingFaceInterface(AbstractModelRegistry):
    model_api_url: str = "https://gastonamengual-object-detection-app.hf.space/"

    @property
    def _client(self) -> Client:
        return Client(self.model_api_url)

    def predict(self, image_data: ImageData) -> ImageData:
        try:
            result = self._client.predict(
                json.dumps(image_data.list_encoded_image),
                api_name="/predict",
            )
            bytes_image = bytes(json.loads(result))
            return ImageData(
                filename=image_data.filename,
                image_bytes=bytes_image,
                model_service=image_data.model_service,
            )

        except Exception as ex:
            raise HuggingFaceException(message=f"HuggingFace API Error: {ex}") from ex
