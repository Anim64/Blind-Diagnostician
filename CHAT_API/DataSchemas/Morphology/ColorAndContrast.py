from pydantic import BaseModel

class ColorAndContrast(BaseModel):
    coreColor: str
    cytoplasmColor: str
    backgroundColor: str
    colorBalance: str

    class Config:
        extra = "forbid"