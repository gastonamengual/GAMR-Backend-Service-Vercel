import json
from dataclasses import dataclass

from gradio_client import Client

from gamr_backend_api_service.ml_service_client import AbstractMLServiceClient
from gamr_backend_api_service.models import ImagePayload

from .errors import HuggingFaceException


@dataclass
class HuggingFaceClient(AbstractMLServiceClient):
    model_api_url: str = "https://gastonamengual-object-detection-app.hf.space/"

    @property
    def _client(self) -> Client:
        return Client(self.model_api_url)

    def predict(self, payload: ImagePayload) -> ImagePayload:
        try:
            result = self._client.predict(
                json.dumps(payload.list_encoded_image),
                api_name="/predict",
            )
            bytes_image = bytes(json.loads(result))
            return ImagePayload(
                filename=payload.filename,
                image_bytes=bytes_image,
                model_service=payload.model_service,
            )

        except Exception as ex:
            raise HuggingFaceException(message=f"HuggingFace API Error: {ex}") from ex
