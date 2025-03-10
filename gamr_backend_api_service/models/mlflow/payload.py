from pydantic import BaseModel


class Dataset(BaseModel):
    X: list[list[float]]
    y: list[int] | None = None


class FlowerPayload(BaseModel):
    data: Dataset
    model_name: str
    model_version: str | None = ""


class Models(BaseModel):
    models: list[str]


class Versions(BaseModel):
    versions: list[int]
