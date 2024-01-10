from flask import request, jsonify, Response
from model import db, Section
from flask_jwt_extended import jwt_required

@jwt_required()
def sectionAPI():
    if request.method == 'GET':
        sections = Section.query.all()
        sections_data = [
            {
                "id": section.id,
                "name": section.name,
                "description": section.description,
                'date_created': section.date_created.isoformat()
            }
            for section in sections
        ]
        return jsonify(sections_data), 200

    if request.method == 'POST':
        data = request.get_json()
        required_keys = ['name', 'description']
        missing_keys = [field for field in required_keys if field not in data]

        if missing_keys:
            return jsonify({"error": f"Missing required keys : {', '.join(missing_keys)}"}), 400

        new_section = Section(
            name=data['name'],
            description=data['description']
        )
        db.session.add(new_section)
        db.session.commit()
        return jsonify({"message": "Section created successfully"}), 201

    if request.method == 'PUT':
        data = request.get_json()
        section = Section.query.get(data.get('id'))
        if section:
            section.name = data.get('name', section.name)
            section.description = data.get('description', section.description)
            db.session.commit()
            return jsonify({"message": "Section updated successfully"}), 200
        return jsonify({"error": "Section not found"}), 404

    if request.method == 'DELETE':
        data = request.get_json()
        section = Section.query.get(data.get('id'))
        if section:
            db.session.delete(section)
            db.session.commit()
            return jsonify({"message": "Section deleted successfully"}), 204
        return jsonify({"error": "Section not found"}), 404
