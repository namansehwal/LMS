from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)
from flask_jwt_extended.exceptions import JWTDecodeError
from model import db, bcrypt, User 


def register_user():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user:
        return jsonify({"message": "User already exists."}), 400

    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    new_user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role="user",
        is_approved=True,
    )
    db.session.add(new_user)
    db.session.commit()
    return (
        jsonify({"message": "User registered successfully!\nLogin To Continue."}),
        201,
    )

def login_user():
    if request.method == 'GET':
        # SUCCESS WELCOME
        return jsonify({"message": "Welcome to the LMS API SERVER!"}), 201