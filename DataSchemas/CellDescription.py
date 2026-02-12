from pydantic import BaseModel
from .Morphology.CentralArea import CentralArea
from .Morphology.ColorAndContrast import ColorAndContrast
from .Morphology.DensityAndDistribution import DensityAndDistribution
from .Morphology.SharpnessAndContours import SharpnessAndContours
from .Morphology.SizeRelations import SizeRelations
from .Morphology.SymetryAndOrientation import SymetryAndOrientation
from .Morphology.TextureAndGranularity import TextureAndGranularity


class CellDescription(BaseModel):
    centralArea: CentralArea
    colorAndContrast: ColorAndContrast
    densityAndDistribution: DensityAndDistribution
    sharpnessAndContours: SharpnessAndContours
    sizeRelations: SizeRelations
    symetryAndOrientation: SymetryAndOrientation
    textureAndGranularity: TextureAndGranularity

    class Config:
        extra = "forbid"