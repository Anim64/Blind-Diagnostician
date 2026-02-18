from langchain_openai import OpenAI

class ModelRegistry:
    def __init__(self, config):
        self.config = config

        self.vlm = self.init_vlm()

    def init_vlm(self):
        return OpenAI(
            model=self.config.models.vlm.name,
            temperature=self.config.models.vlm.temperature
        )
