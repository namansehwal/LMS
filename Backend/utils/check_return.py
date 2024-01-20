from datetime import datetime
from model import AccessLog, db

def update_access_logs():
    issued_logs = AccessLog.query.filter_by(status='Issued').all()

    for log in issued_logs:
        if datetime.now() > log.due_date:
            log.status = 'Revoked'
            db.session.commit()