from flask import request, jsonify
from model import db, Request, User, Book
from flask_jwt_extended import jwt_required
from datetime import datetime
# @jwt_required()
def book_request():
    if request.method == 'GET':
        books_query = Request.query.all()
        books = []
        for book in books_query:
            books.append(book.__serialize__())
        return jsonify(books), 200
    
    if request.method == 'POST':
        data = request.get_json()
        required_keys = ['user_id', 'book_id']
      

        #check user_id and book_id exists in database
        user_id = User.query.get(data.get('user_id'))
        book_id = Book.query.get(data.get('book_id'))
        if not user_id:
            return jsonify({"error": "User not found"}), 404
        if not book_id:
            return jsonify({"error": "Book not found"}), 404

        missing_keys = [key for key in required_keys if key not in data]

        if missing_keys:
            return jsonify({"error": f"Missing required keys : {', '.join(missing_keys)}"}), 400

        new_book = Request(
            user_id=data['user_id'],
            book_id=data['book_id'],
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book created successfully"}), 201
    
    #define put method to approve/deny requests

    if request.method == 'PUT':
        data = request.get_json()
        book = Request.query.get(data.get('id'))
        
        if book:
            if data.get('approved') == "True":
                setattr(book, 'status', 'Approved')
                setattr(book, 'approved_date', str(datetime.now()))
                db.session.commit()
                return jsonify({"message": "Book request approved"}), 200
            
            elif data.get('approved') == "False":
                setattr(book, 'status', 'Rejected')
                db.session.commit()
                return jsonify({"message": "Book request rejected"}), 200
        else:
                return jsonify({"message": "Book request not found!!"}), 400
    
  
