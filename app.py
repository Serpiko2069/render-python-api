from fastapi import FastAPI
from pydantic import BaseModel
import scripts.transcribe as transcribe_script

app = FastAPI()

class TranscribeRequest(BaseModel):
    input_path: str
    output_path: str = "output.srt"
    model_size: str = "small"

@app.post("/transcribe")
def transcribe_endpoint(request: TranscribeRequest):
    # Вызываем функцию транскрибации из твоего скрипта
    transcribe_script.transcribe_to_srt(
        input_path=request.input_path,
        output_path=request.output_path,
        model_size=request.model_size
    )

    # Читаем результат и возвращаем содержимое SRT
    with open(request.output_path, "r", encoding="utf-8") as f:
        srt_data = f.read()

    return {
        "status": "success",
        "output_path": request.output_path,
        "srt": srt_data
    }
