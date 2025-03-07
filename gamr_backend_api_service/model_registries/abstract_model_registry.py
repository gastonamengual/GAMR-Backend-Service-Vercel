from abc import ABC, abstractmethod
from dataclasses import dataclass

from gamr_backend_api_service.models import ImageData


@dataclass
class AbstractModelRegistry(ABC):
    @abstractmethod
    def predict(self, image_data: ImageData) -> ImageData: ...
