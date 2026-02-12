from pydantic import BaseModel

class SizeRelations(BaseModel):
    coreSizeVariability: str
    coreCytoplasmSizeRatio: str
    dominantStructureSize: str

    class Config:
        extra = "forbid"