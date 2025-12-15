"""Simple STT placeholder service."""
def transcribe(audio_bytes: bytes) -> str:
    """Placeholder transcription: returns a synthetic message."""
    if not audio_bytes:
        return ""
    return f"transcribed {len(audio_bytes)} bytes"
