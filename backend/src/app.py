from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route('/user/', methods=['GET'])
def get_user():
    email = request.args.get('email')
    client = pymongo.MongoClient('mongodb://database:27017/', username='bankuser', password='bankpassword', authSource='bank')
    db = client['bank']
    collection = db['users']

    user = collection.find_one({"email": email})
    if user:
        return jsonify({"name": user["name"], "email": user["email"]}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
# TODO: test this functionality
@app.route('/transfer/', methods=['GET'])
def transfer():
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    amount = request.args.get('amount')
    client = pymongo.MongoClient('mongodb://database:27017/', username='bankuser', password='bankpassword', authSource='bank')
    db = client['bank']
    collection = db['users']

    sender = collection.find_one({"email": sender})
    receiver = collection.find_one({"email": receiver})
    if sender and receiver:
        if sender["balance"] >= amount:
            sender["balance"] -= amount
            receiver["balance"] += amount
            collection.update_one({"email": sender["email"]}, {"$set": {"balance": sender["balance"]}})
            collection.update_one({"email": receiver["email"]}, {"$set": {"balance": receiver["balance"]}})
            return jsonify({"message": "Transfer successful"}), 200
        else:
            return jsonify({"error": "Insufficient balance"}), 400
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
