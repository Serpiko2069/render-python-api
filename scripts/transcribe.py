def transcribe_to_srt(input_path: str, output_path: str = "output.srt", model_size: str = "small"):
    # Заглушка для теста всей цепочки Make + FastAPI + Google Sheets
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("Test OK — всё дошло до Render!\n")
