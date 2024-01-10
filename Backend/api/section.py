from flask import request, jsonify

from model import db, Section, Book

def sectionAPI():
    if request.method == 'GET':
        sections = Section.query.all()
        sections = [
            {
                "id": section.id,
                "name": section.name,
                "description": section.description,
                'date_created': section.date_created
            }
            for section in sections
        ]
        return jsonify(sections)


    if request.method == 'POST':
        data = request.get_json()
        section = Section(
            name=data['name'],
            description=data['description']
        )
        db.session.add(section)
        db.session.commit()
        return jsonify({"message": "Section created successfully!"}), 201


    if request.method == 'PUT':
        data = request.get_json()
        section = Section.query.get(data['id'])
        section.name = data['name']
        section.description = data['description']
        db.session.commit()
        return jsonify({"message": "Section updated successfully!"}), 201
    
    if request.method == 'DELETE':
        data = request.get_json()
        section = Section.query.get(data['id'])
        db.session.delete(section)
        db.session.commit()
        return jsonify({"message": "Section deleted successfully!"}), 201
    

def bookAPI():
    if request.method == 'GET':
        books = Book.query.all()
        books = [
            {
                "id": book.id,
                "name": book.name,
                "content": book.content,
                'isbn': book.isbn,
                'author': book.author,
                'date_issued': book.date_issued,
                'return_date': book.return_date,
                'section_id': book.section_id,
            }
            for book in books
        ]
        return jsonify(books)


    if request.method == 'POST':
        data = request.get_json()
        book = Book(
            name=data['name'],
            content=data['content'],
            isbn=data['isbn'],
            author=data['author'],
            section_id=data['section_id'],
        )
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book created successfully!"}), 201


    if request.method == 'PUT':
        data = request.get_json()
        book = Book.query.get(data['id'])
        book.name = data['name']
        book.content = data['content']
        book.isbn = data['isbn']
        book.author = data['author']
        book.section_id=data['section_id']
        db.session.commit()
        return jsonify({"message": "Book updated successfully!"}), 201
    
    if request.method == 'DELETE':
        data = request.get_json()
        book = Book.query.get(data['id'])
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully!"}), 201