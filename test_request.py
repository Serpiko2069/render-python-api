import requests

url = "https://render-python-api-x4j5.onrender.com/transcribe"  # замени на свой URL если другой

payload = {
    "input_path": "Urok.mp3",
    "output_path": "Urok.srt",
    "model_size": "small"
}

response = requests.post(url, json=payload)

print("📤 Запрос отправлен:")
print(payload)
print("📥 Ответ сервера:")
print(response.json())
