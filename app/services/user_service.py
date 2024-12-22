from flask import jsonify
from app.models.user import User
from app.utils.db import mongo

def create_user(username, email, password):
    if mongo.db.users.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400
    new_user = User(username=username, email=email, password=password)
    mongo.db.users.insert_one(new_user.to_dict())
    return jsonify({"message": "User created successfully"}), 201

def get_user(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

def delete_user(user_id):
    result = mongo.db.users.delete_one({"_id": user_id})
    if result.deleted_count:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

def update_user(user_id, updates):
    result = mongo.db.users.update_one({"_id": user_id}, {"$set": updates})
    if result.modified_count:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"error": "User not found or no changes made"}), 404