from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.ai import chat_response

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat(body: ChatRequest):
    resp = chat_response(body.prompt)
    return ChatResponse(response=resp)
