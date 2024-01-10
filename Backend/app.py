from flask import Flask
from config import Config
from model import db

app = Flask(__name__)
app.config.from_object(Config)



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)    