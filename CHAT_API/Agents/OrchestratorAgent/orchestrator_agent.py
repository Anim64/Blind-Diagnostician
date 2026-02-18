from langgraph.graph import StateGraph
from typing import TypedDict, List

from CHAT_API.Agents.ImageDescriptionAgent.image_description_agent import ImageDescriptionAgent
from CHAT_API.DataSchemas.Morphology.CentralArea import CentralArea

class GraphState(TypedDict):
    message: str
    images: List[str]
    descriptions: List[CentralArea]

image_agent = ImageDescriptionAgent()

async def image_node(state: GraphState):
    descriptions = await image_agent.describe(state["images"])
    return {"descriptions": descriptions}

def build_graph():
    workflow = StateGraph(GraphState)

    workflow.add_node("image_node", image_node)

    workflow.set_entry_point("image_node")

    workflow.set_finish_point("image_node")

    return workflow.compile()