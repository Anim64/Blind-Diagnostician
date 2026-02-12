from pydantic import BaseModel

class SymetryAndOrientation(BaseModel):
    directionalStructureOrientation: str
    compositionalSymetry: str
    areaLayout: str

    class Config:
        extra = "forbid"