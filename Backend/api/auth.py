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
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(username=data["email"]).first()

        if user:
            return jsonify({"message": "User already exists."}), 400

        hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        new_user = User(
            username=data["username"],
            email=data["email"],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return (
            jsonify({"message": "User registered successfully!\nLogin To Continue."}),
            201,
        )

def login_user():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(email=data["email"]).first()

        if not user:
            return jsonify({"message": "User does not exist."}), 404

        if not bcrypt.check_password_hash(user.password, data["password"]):
            return jsonify({"message": "Invalid credentials. Wrong Password Entered!!"}), 401

        access_token = create_access_token(identity=user.id)
        

        return jsonify({"access_token": access_token,
                        "role": user.user_type,
                        "username": user.username,
                        "email": user.email,   
                        'user_id': user.id,
                        }), 200

@jwt_required()
def user_details():
    return jsonify({"message": "You made it to the secure route.", }), 200
    # current_user = get_jwt_identity()
    # # add user id to jwt_identity
    # current_user["id"] = (
    #     User.query.filter_by(username=current_user["username"]).first().id
    # )

    # return jsonify(logged_in_as=current_user), 200


    