from pydantic import BaseModel


class RecognizeResponse(BaseModel):
    text: str


class TTSRequest(BaseModel):
    text: str


class TTSResponse(BaseModel):
    audio_b64: str


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str
