from flask import request, jsonify
from model import db, Book
from flask_jwt_extended import jwt_required

@jwt_required()
def bookAPI():
    if request.method == 'GET':
        books_query = Book.query.all()
        books = []
        for book in books_query:
            books.append(book.__serialize__())
        return jsonify(books), 200

    if request.method == 'POST':
        data = request.get_json()
        required_keys = ['name', 'content', 'isbn', 'author', 'section_id']
        missing_keys = [key for key in required_keys if key not in data]

        if missing_keys:
            return jsonify({"error": f"Missing required keys : {', '.join(missing_keys)}"}), 400

        new_book = Book(
            name=data['name'],
            content=data['content'],
            isbn=data['isbn'],
            author=data['author'],
            section_id=data['section_id'],
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book created successfully"}), 201


    if request.method == 'PUT':
        data = request.get_json()
        book = Book.query.get(data.get('id'))
        if book:
            for key in data:
                if key in ['name', 'content', 'isbn', 'author', 'section_id']:
                    setattr(book, key, data[key])
            db.session.commit()
            return jsonify({"message": "Book updated successfully"}), 200
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'DELETE':
        data = request.get_json()
        book = Book.query.get(data.get('id'))
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book deleted successfully"}), 204
        return jsonify({"error": "Book not found"}), 404
