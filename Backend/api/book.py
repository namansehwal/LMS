from flask import request, jsonify
from model import db, Book, BookRequest, AccessLog, Rating
from flask_jwt_extended import jwt_required
from datetime import datetime


# @jwt_required()
def bookAPI():
    if request.method == "GET":
        books_query = Book.query.all()
        books = []
        for book in books_query:
            books.append(book.__serialize__())
        return jsonify(books), 200

    if request.method == "POST":
        data = request.get_json()
        required_keys = [
            "name",
            "content",
            "isbn",
            "author",
            "section_id",
            "number_of_pages",
            "image_url",
            "pdf_url",
            "epub_url",
            "price"
        ]
        missing_keys = [key for key in required_keys if key not in data]

        if missing_keys:
            return (
                jsonify(
                    {"error": f"Missing required keys : {', '.join(missing_keys)}"}
                ),
                400,
            )

        new_book = Book(
            name=data["name"],
            content=data["content"],
            isbn=data["isbn"],
            author=data["author"],
            section_id=data["section_id"],
            #number_of_pages=data.get("number_of_pages"),
            number_of_pages=data["number_of_pages"],
            image_url=data["image_url"],
            pdf_url=data["pdf_url"],
            epub_url=data["epub_url"],
            price=data["price"]
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book created successfully"}), 201

    if request.method == "PUT":
        data = request.get_json()
        book = Book.query.get(data.get("id"))
        if book:
            for key in data:
                if key in [
                    "name",
                    "content",
                    "isbn",
                    "author",
                    "section_id",
                    "number_of_pages",
                    "image_url",
                    "pdf_url",
                    "epub_url",
                    "price"
                ]:
                    setattr(book, key, data[key])
                    setattr(book, "date_updated", datetime.now())
            db.session.commit()
            return jsonify({"message": "Book updated successfully"}), 200
        return jsonify({"error": "Book not found"}), 404

    if request.method == "DELETE":
        data = request.get_json()
        book = Book.query.get(data.get("id"))
        if book:
            ratings = Rating.query.filter_by(book_id=book.id).all()
            if ratings:
                for rating in ratings:
                    db.session.delete(rating)
            access = AccessLog.query.filter_by(book_id=book.id).all()
            if access:
                for log in access:
                    db.session.delete(log)
            book_requests = BookRequest.query.filter_by(book_id=book.id).all()
            if book_requests:
                for book_request in book_requests:
                    db.session.delete(book_request)
            db.session.commit()

            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book deleted successfully"}), 204
        return jsonify({"error": "Book not found"}), 404
