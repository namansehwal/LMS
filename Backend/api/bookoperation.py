from flask import request, jsonify
from model import db, Request, User, Book, AccessLog, Rating
from flask_jwt_extended import jwt_required
from datetime import datetime


# @jwt_required()
def book_request():
    if request.method == 'GET':
        books_query = Request.query.all()
        books = []
        for book in books_query:
            book.user_id =  User.query.get(book.user_id).username 
            book.book_id =   Book.query.get(book.book_id).name
                        
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
        return jsonify({"message": "Book request created successfully \nPending for approval by Librarian.."}), 201
    
    #define put method to approve/deny requests

    if request.method == 'PUT':
        data = request.get_json()
        book = Request.query.get(data.get('id'))
        
        if book:
            if data.get('approved') == "True":

                setattr(book, 'status', 'Approved')
                setattr(book, 'approved_date', datetime.now())
                new_access_log = AccessLog(
                    user_id=book.user_id,
                    book_id=book.book_id )    
                db.session.add(new_access_log)
                db.session.commit()

                return jsonify({"message": "Successfully, Book request approved"}), 200
            
            elif data.get('approved') == "False":
                setattr(book, 'status', 'Rejected')
                db.session.commit()
                return jsonify({"message": "Successfully, book request rejected"}), 200
        else:
                return jsonify({"message": "Error, Book request not found!!"}), 400
    
  

def BookAccess():
    if request.method == 'GET':
        
        books_query = AccessLog.query.all()
        books = []
        for book in books_query:
            books.append(book.__serialize__())
        return jsonify(books), 200

    
    #define put method to return book and update status as returned and return date
    if request.method == 'PUT':
        data = request.get_json()
        book = AccessLog.query.get(data.get('id'))
        
        if book:
            if data.get('returned') == "True":
                setattr(book, 'status', 'Returned')
                setattr(book, 'return_date', datetime.now())
                db.session.commit()
                return jsonify({"message": "Successfully, Book returned"}), 200
        else:
                return jsonify({"message": "Error, Book Access log not found!!"}), 400

def BookRating():
    if request.method == 'GET':

        books_query = Rating.query.all()
        books = []
        for book in books_query:
            books.append(book.__serialize__())
        return jsonify(books), 200
    
    if request.method == 'POST':
        #    def __init__(self, user_id, book_id, rating_value):
        data = request.get_json()
        required_keys = ['user_id', 'book_id', 'rating_value']

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
        
        # check if user has already rated the book
        rating = Rating.query.filter_by(user_id=data.get('user_id'), book_id=data.get('book_id')).first()

        if rating:
            #update rating
            setattr(rating, 'rating_value', data.get('rating_value'))
            db.session.commit()
            return jsonify({"message": "Successfully, Book rating updated"}), 200
        

        new_book = Rating(
            user_id=data['user_id'],
            book_id=data['book_id'],
            rating_value=data['rating_value']
        )
        db.session.add(new_book)
        db.session.commit()

        return jsonify({"message": "Book rating created successfully"}), 201        
     