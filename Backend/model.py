from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)
    last_login = db.Column(db.DateTime)

    def __init__(self, username, email, password, user_type="user"):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type


class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), nullable=False)

    def __init__(self, token):
        self.token = token


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)

    def __init__(self, name, description):
        self.name = name
        self.date_created = datetime.now()
        self.description = description


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    number_of_pages = db.Column(db.Integer)
    isbn = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)
    section_id = db.Column(db.Integer, db.ForeignKey("section.id"), nullable=False)
    section = db.relationship("Section", backref=db.backref("books", lazy=True))

    def __init__(self, name, content, isbn, author, section_id, number_of_pages):
        self.name = name
        self.content = content
        self.isbn = isbn
        self.author = author
        self.number_of_pages = number_of_pages
        self.date_created = datetime.now()
        self.date_updated = datetime.now()
        self.section_id = section_id

    def __serialize__(self):
        return {
            "id": self.id,
            "name": self.name,
            "content": self.content,
            "isbn": self.isbn,
            "author": self.author,
            "date_created": self.date_created,
            "date_updated": self.date_updated,
            "section_id": self.section_id,
            "number_of_pages": self.number_of_pages,
        }


class BookRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    username = db.Column(db.String(50))
    book_name = db.Column(db.String(100))
    request_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Pending/Approved
    approved_date = db.Column(db.DateTime)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.username = User.query.get(user_id).username
        self.book_name = Book.query.get(book_id).name
        self.request_date = datetime.now()
        self.status = "Pending"

    def __serialize__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "username": self.username,
            "book_name": self.book_name,
            "request_date": self.request_date,
            "status": self.status,
            "approved_date": self.approved_date,
        }


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    rating_value = db.Column(db.Integer, nullable=False)
    date_rated = db.Column(db.DateTime)

    def __init__(self, user_id, book_id, rating_value):
        self.user_id = user_id
        self.book_id = book_id
        self.rating_value = rating_value
        self.date_rated = datetime.now()

    def __serialize__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "rating_value": self.rating_value,
            "date_rated": self.date_rated,
        }


class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    username = db.Column(db.String(50))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    book_name = db.Column(db.String(100))
    status = db.Column(db.String(10), nullable=False)  # Issued / Returned
    issue_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.status = "Issued"
        self.username = User.query.get(user_id).username
        self.book_name = Book.query.get(book_id).name
        self.issue_date = datetime.now()
        self.return_date = datetime.now() + timedelta(days=7)

    def __serialize__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "username": self.username,
            "book_name": self.book_name,
            "status": self.status,
            "issue_date": self.issue_date,
            "return_date": self.return_date,
        }
