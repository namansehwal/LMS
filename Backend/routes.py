from api.auth import register_user, login_user, user_details
from api.section import sectionAPI
from api.book import bookAPI
from api.bookoperation import book_request

from app import app


# Auhtentication Routes
app.add_url_rule("/register", view_func=register_user, methods=["POST"])
app.add_url_rule("/login", view_func=login_user, methods=["POST"])
app.add_url_rule("/user", view_func=user_details, methods=["GET"])


# Section Routes
app.add_url_rule("/section", view_func=sectionAPI, methods=["GET", "POST", "PUT", "DELETE"])



# Book Operation Routes
app.add_url_rule("/book", view_func=bookAPI, methods=["GET", "POST", "PUT", "DELETE"])
app.add_url_rule("/book/request", view_func=book_request, methods=["GET", "POST", "PUT"])

