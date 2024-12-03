from pydantic import BaseModel

class InferenceResultEntity(BaseModel):
    encoded_image: str
    object: list[str]
    coordinate: list[int]

class InferenceEntity(BaseModel):
    image: bytes
    object: list[str]
    coordinate: list[int]

