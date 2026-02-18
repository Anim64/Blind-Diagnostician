from pydantic import BaseModel

class VLMConfig(BaseModel):
    name: str
    temperature: float

class ModelConfig(BaseModel):
    vlm: VLMConfig

class AppConfig(BaseModel):
    models: ModelConfig