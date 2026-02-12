from pydantic import BaseModel

class DensityAndDistribution(BaseModel):
    imageCenterStructureDensity: str
    distributionTowardEdges: str

    class Config:
        extra = "forbid"