from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.security import get_api_key
from app.services.llm_service import LLMService
from app.services.vector_service import VectorService

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    top_k: int = 5

class ChatResponse(BaseModel):
    answer: str
    sources: list = []

# instantiate service singletons (simple approach)
llm = LLMService()
vect = VectorService()

@router.post("/query", response_model=ChatResponse, dependencies=[Depends(get_api_key)])
async def query_chat(body: ChatRequest):
    # 1) find relevant context from vector DB
    hits = vect.search(body.query, top_k=body.top_k)

    # 2) build a prompt + call LLM
    prompt = llm.build_prompt(body.query, hits)
    answer = await llm.complete(prompt)

    return ChatResponse(answer=answer, sources=[h["id"] for h in hits])
