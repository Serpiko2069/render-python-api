def transcribe_to_srt(input_path: str, output_path: str = "output.srt", model_size: str = "small"):
    # Заглушка для теста деплоя: просто пишет тестовую строку в файл SRT
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("00:00:00,000 --> 00:00:02,000\nПример субтитров\n")
