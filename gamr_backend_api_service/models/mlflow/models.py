from pydantic import BaseModel


class Models(BaseModel):
    models: list[str]
