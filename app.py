from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    print("📥 Получены данные:", data)
    return jsonify({"status": "ok", "message": "Данные получены!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
