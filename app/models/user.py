from flask import current_app
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

mongo = PyMongo()

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    @staticmethod
    def create_user(username, email, password):
        user = User(username, email, password)
        mongo.db.users.insert_one({
            'username': user.username,
            'email': user.email,
            'password': user.password
        })
        return user

    @staticmethod
    def get_user_by_username(username):
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def get_user_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def delete_user(username):
        mongo.db.users.delete_one({'username': username})

    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)