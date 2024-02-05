from celery import shared_task, Celery
from utils.mail_hog import send_email
from datetime import datetime
from utils.email_templates import create_html_reminder, create_html_report, google_chat_webhook
from model import User


@shared_task(ignore_result=True)
def daily_reminders():
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    Users = User.query.filter_by(user_type='user').all()
    
    for user in Users:
        if user.last_login != current_date:
            html_reminder = create_html_reminder(user)
            send_email(user.email, 'Reminder', html_reminder)
            print('Reminder sent to', user.username)
            google_chat_webhook(user.username)
    

    
            