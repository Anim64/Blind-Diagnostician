from pydantic import BaseModel

class CentralArea(BaseModel):
    mainStructureCount: str
    shape: str
    layout: str
    distanceBetweenStructures: str

    class Config:
        extra = "forbid"