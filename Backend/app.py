from flask import Flask
from config import Config
from model import db, bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
from routes import *
bcrypt.init_app(app)
jwt = JWTManager(app)

CORS(app, resources={r"/*": {"origins": "*"}})



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()

        # Create Librarian as Admin if not exists
        from utils.librarian_setup import librarian_setup
        librarian_setup()   


    app.run(debug=True)    