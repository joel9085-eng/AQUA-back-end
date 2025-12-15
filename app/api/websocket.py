from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # simple echo for now; replace with AI-driven responses later
            await websocket.send_text(f"echo: {data}")
    except WebSocketDisconnect:
        return
