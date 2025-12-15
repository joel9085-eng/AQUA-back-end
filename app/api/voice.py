from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services import stt, tts
from app.models import schemas

router = APIRouter()


@router.post("/recognize", response_model=schemas.RecognizeResponse)
async def recognize_audio(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = stt.transcribe(content)
        return schemas.RecognizeResponse(text=text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/speak", response_model=schemas.TTSResponse)
async def speak_text(body: schemas.TTSRequest):
    try:
        audio_b64 = tts.synthesize(body.text)
        return schemas.TTSResponse(audio_b64=audio_b64)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
