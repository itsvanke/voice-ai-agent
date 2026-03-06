
from fastapi import APIRouter, WebSocket
from backend.controllers.voice_controller import handle_voice

router = APIRouter()

@router.websocket("/voice")
async def voice_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        audio = await websocket.receive_bytes()
        response_audio = await handle_voice(audio)
        await websocket.send_bytes(response_audio)
