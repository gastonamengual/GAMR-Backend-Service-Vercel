from enum import StrEnum, auto

from .abstract_model_registry import AbstractModelRegistry
from .hugging_face.hf_model_registry import HuggingFaceInterface


class ModelService(StrEnum):
    HuggingFace = auto()


def get_ai_model_interface(interface: ModelService) -> AbstractModelRegistry:
    match interface:
        case ModelService.HuggingFace:
            return HuggingFaceInterface  # type: ignore


__all__ = ["AbstractModelRegistry", "HuggingFaceInterface"]
