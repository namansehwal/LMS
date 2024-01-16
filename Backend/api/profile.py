from flask import request, jsonify
from model import db, User, AccessLog, Rating, BookRequest

def UserProfile():
   # this function is used to get the user profile and update the user profile only Username and Email
    if request.method == "GET":
        data = request.get_json()
        user = User.query.get(data.get("id"))
        if not user:
            return jsonify({"error": "User not found"}), 404
        result = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at
        }
        return jsonify(result), 200
        
    
    if request.method == "PUT":
        data = request.get_json()
        user = User.query.get(data.get("id"))
        if user:
            try:
                user.username = data.get("username", user.username)
                user.email = data.get("email", user.email)
                db.session.commit()
                return jsonify({"message": "User updated successfully"}), 200
            except Exception as e:
                # Handle database update errors
                db.session.rollback()
                return jsonify({"error": str(e)}), 500
        return jsonify({"error": "User not found"}), 404

      #make a delete request to delete the user profile
    if request.method == "DELETE":

        data = request.get_json()
        user = User.query.get(data.get("id"))

        if user:

            try:
                #delete user from each table database

                #delete user from AccessLog table
                access_log = AccessLog.query.filter_by(user_id=user.id).all()
                for access in access_log:
                    db.session.delete(access)
                    db.session.commit()

                #delete user from Rating table
                rating = Rating.query.filter_by(user_id=user.id).all()
                for rate in rating:
                    db.session.delete(rate)
                    db.session.commit()

                #delete user from BookRequest table
                book_request = BookRequest.query.filter_by(user_id=user.id).all()
                for book in book_request:
                    db.session.delete(book)
                    db.session.commit()


                db.session.delete(user)
                db.session.commit()
                return jsonify({"message": "User deleted successfully"}), 200
            except Exception as e:
                # Handle database update errors
                db.session.rollback()
                return jsonify({"error": str(e)}), 500
        return jsonify({"error": "User not found"}), 404  