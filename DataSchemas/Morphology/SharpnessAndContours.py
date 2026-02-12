from pydantic import BaseModel

class SharpnessAndContours(BaseModel):
    coreContour: str
    cytoplasmEdges: str
    intraCoreStructurePresence: str

    class Config:
        extra = "forbid"