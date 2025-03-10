from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


@dataclass
class AbstractMLServiceClient(ABC):
    @abstractmethod
    def predict(self, payload: Any) -> BaseModel: ...
