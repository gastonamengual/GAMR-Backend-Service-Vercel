from dataclasses import dataclass

from fastapi import status


@dataclass
class HuggingFaceException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = ""
