from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
users = [
    {"id": 1, "name": "Saurabh"},
    {"id": 2, "name": "Rahul"}
]

# GET API
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST API
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    users.append(data)
    return jsonify({
        "message": "User created",
        "user": data
    }), 201

# PUT API
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user)

    return jsonify({"message": "User not found"}), 404

# DELETE API
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]

    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
