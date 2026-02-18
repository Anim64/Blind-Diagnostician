from contextlib import asynccontextmanager
from fastapi import FastAPI

from CHAT_API.API.app_schemas import ChatRequest, ChatResponse
from CHAT_API.Agents.OrchestratorAgent.orchestrator_agent import build_graph



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing system...")
    app.state.orchestrator = build_graph()
    print("System ready...")

    yield

    print("Shutting down...")

    
app = FastAPI(title="Blind Diagnostician",
              lifespan=lifespan)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    orchestrator = app.state.orchestrator

    result = orchestrator.ainvoke({
        "message": request.message,
        "images": request.images,
        "descriptions": []
        }
    )

    return ChatResponse(descriptions=result["descriptions"])
    

