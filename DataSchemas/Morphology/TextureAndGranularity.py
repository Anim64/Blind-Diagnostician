from pydantic import BaseModel

class TextureAndGranularity(BaseModel):
    coreTexture: str
    cytoplasmTexture: str
    background: str
    textureEdge: str
    
    class Config:
        extra = "forbid"