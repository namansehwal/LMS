from datetime import datetime, timedelta
from model import AccessLog, db

def update_access_logs():
    issued_logs = AccessLog.query.filter_by(status='Issued').all()

    for log in issued_logs:
        if datetime.utcnow() > log.due_date:
            log.status = 'Revoked'
            log.revoke_date = datetime.utcnow()
            db.session.commit()