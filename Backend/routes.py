from api.auth import register_user, login_user
from api.section import sectionAPI
from app import app


# Auhtentication Routes
app.add_url_rule("/register", view_func=register_user, methods=["POST"])
app.add_url_rule("/login", view_func=login_user, methods=["GET"])



# Section Routes
app.add_url_rule("/section", view_func=sectionAPI, methods=["GET", "POST", "PUT", "DELETE"])