from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # Librarian/GeneralUser


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
    isbn = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    date_issued = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    section = db.relationship('Section', backref=db.backref('books', lazy=True))

    def __init__(self, name, content, isbn, author, section_id):
        self.name = name
        self.content = content
        self.isbn = isbn
        self.author = author
        self.date_issued = datetime.now()
        self.return_date = datetime.now()
        self.section_id = section_id

    def __serialize__(self):
        return {
            "id": self.id,
            "name": self.name,
            "content": self.content,
            "isbn": self.isbn,
            "author": self.author,
            "date_issued": self.date_issued,
            "return_date": self.return_date,
            "section_id": self.section_id
        }


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    request_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Pending/Approved/Rejected

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    rating_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    date_rated = db.Column(db.DateTime)

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    action = db.Column(db.String(10), nullable=False)  # Issue/Return
    log_date = db.Column(db.DateTime, nullable=False)
