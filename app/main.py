from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import voice, chat, websocket
from app.config import settings

app = FastAPI(title="AQUA-back-end")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice.router, prefix="/voice", tags=["voice"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(websocket.router, prefix="/ws", tags=["websocket"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.DEBUG)
