from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

from scripts.transcribe import transcribe_to_srt

app = FastAPI()

class TranscribeRequest(BaseModel):
    input_path: str
    output_path: str = "output.srt"
    model_size: str = "small"

@app.post("/transcribe")
async def transcribe_endpoint(request: TranscribeRequest):
    try:
        transcribe_to_srt(
            input_path=request.input_path,
            output_path=request.output_path,
            model_size=request.model_size
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription error: {e}")

    if not os.path.isfile(request.output_path):
        raise HTTPException(status_code=404, detail=f"SRT file not found: {request.output_path}")

    try:
        with open(request.output_path, "r", encoding="utf-8") as f:
            srt_data = f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Read file error: {e}")

    return {
        "status": "success",
        "output_path": request.output_path,
        "srt": srt_data
    }
