from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import PydanticOutputParser
from CHAT_API.DataSchemas.Morphology.CentralArea import CentralArea
from config import OPEN_API_KEY

STRUCTURE_PROMPT = """
You are a medical image analysis assistant.

Look ONLY for the following features under "Structure":

Central area:
- Main structure count (e.g. cores)
- Shape (oval, circular, irregular, deformed)
- Layout (compact, uniform, overlapping)
- Distance between structures (small, medium, large)

For EACH provided image:
- Describe EACH of these features separately.
- Output must strictly follow the JSON schema.
- Maximum 4 sentences per feature.
- Do NOT invent features not visible.
- Do NOT describe anything outside this structure.
"""

class ImageDescriptionAgent():
    def __init__(self):
        self.vlm = ChatOpenAI(
            model="gpt-4o",
            api_key=OPEN_API_KEY,
            temperature=0
        )

        self.parser = PydanticOutputParser(pydantic_object=CentralArea)
    
    async def describe(self, images_base64: list[str]) -> list[CentralArea]:
        descriptions = list[str]

        for image in images_base64:
            message = [
                SystemMessage(content=STRUCTURE_PROMPT),
                HumanMessage(
                    content=[
                        {"type": "text", "text": "Analyze this bone marrow cell image."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image}"
                            },
                        },
                    ]
                )
            ]

            response = await self.vlm.ainvoke(message)
            descriptions.append(self.parser.parse(response.content))
        
        return descriptions