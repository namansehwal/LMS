from flask import Flask
from config import Config
from model import db, bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from utils.celery_worker import celery_init_app
from celery.schedules import crontab

app = Flask(__name__)
celery_app = celery_init_app(app)
app.config.from_object(Config)

from routes import *
bcrypt.init_app(app)  #password hashing
jwt = JWTManager(app)  #JSON Web Tokens


CORS(app, resources={r"/*": {"origins": "*"}})



#✌️❤️📚
# Run monthly activity report every minute  
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    
    # Run monthly activity report every minute
    sender.add_periodic_task(crontab(minute='*', hour='*'), tasks.monthly_activity_report.s())





if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()

        # Create Librarian as Admin if not exists
        from utils.librarian_setup import librarian_setup
        librarian_setup()   
        
        # check if book is returned
        from utils.check_return import update_access_logs
        update_access_logs()

    app.run(debug=True)    