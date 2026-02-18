from pydantic import BaseModel
from typing import List

from CHAT_API.DataSchemas.Morphology.CentralArea import CentralArea

class ChatRequest(BaseModel):
    message: str
    images: List[str]  # base64 images from frontend

class ChatResponse(BaseModel):
    descriptions: List[CentralArea]