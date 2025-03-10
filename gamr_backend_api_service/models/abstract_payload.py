from abc import ABC

from pydantic import BaseModel


class AbstractPayload(BaseModel, ABC): ...
