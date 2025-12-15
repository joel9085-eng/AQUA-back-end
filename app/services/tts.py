"""Simple TTS placeholder service that returns base64-encoded bytes."""
import base64


def synthesize(text: str) -> str:
    """Return base64-encoded bytes representing the audio payload.

    This is a placeholder. Replace with a real TTS implementation.
    """
    if text is None:
        text = ""
    data = text.encode("utf-8")
    return base64.b64encode(data).decode("utf-8")
