from flask import request, jsonify

from model import db, Section

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