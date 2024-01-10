from model import User, db, bcrypt

def librarian_setup():
    
    if not User.query.filter_by(email='librarian@gmail.com').first():
                
                new_user = User(
                    username='librarian',
                    email='librarian@gmail.com',
                    password= bcrypt.generate_password_hash('librarian').decode("utf-8"),
                    user_type='admin'
                    )
                
                db.session.add(new_user)
                db.session.commit()