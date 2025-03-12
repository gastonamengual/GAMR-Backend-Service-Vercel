from pydantic import BaseModel


class Versions(BaseModel):
    versions: list[int]
