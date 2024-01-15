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

    def __init__(self, username, email, password, user_type='user'):
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
    status = db.Column(db.String(20), nullable=False)  # Pending/Approved
    approved_date = db.Column(db.DateTime)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.request_date = datetime.now()
        self.status = 'Pending'

    def __serialize__(self):
        return {
            "id": self.id,
            # user_id with name
            "user_id": self.user_id + ' ' + self.user.username,
            "book_id": self.book_id,
            "request_date": self.request_date,
            "status": self.status,
            "approved_date": self.approved_date
        }

        

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
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
            "date_rated": self.date_rated
        }    

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    status = db.Column(db.String(10), nullable=False)  # Issued / Returned 
    issue_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.status = 'Issued'
        self.issue_date = datetime.now()
        self.return_date = datetime.now() + timedelta(days=7)

    def __serialize__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "status": self.status,
            "issue_date": self.issue_date,
            "return_date": self.return_date
        }    
