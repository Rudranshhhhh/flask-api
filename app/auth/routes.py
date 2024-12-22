from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app.models.user import User
from app.auth.utils import send_recovery_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.find_by_username(username)
    if user and user.verify_password(password):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    return jsonify(message='Invalid credentials'), 401

@auth_bp.route('/recover', methods=['POST'])
def recover():
    data = request.get_json()
    email = data.get('email')
    
    user = User.find_by_email(email)
    if user:
        send_recovery_email(user)
        return jsonify(message='Recovery email sent'), 200
    return jsonify(message='User not found'), 404

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if User.find_by_username(username):
        return jsonify(message='Username already exists'), 400
    
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    new_user.save()
    
    return jsonify(message='User created successfully'), 201

@auth_bp.route('/user/<username>', methods=['DELETE'])
@jwt_required()
def delete_user(username):
    user = User.find_by_username(username)
    if user:
        user.delete()
        return jsonify(message='User deleted successfully'), 200
    return jsonify(message='User not found'), 404