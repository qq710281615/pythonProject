from main import app
from view import *
app.add_url_rule("/", view_func=index_1, methods=["post", "get"], endpoint="qwer")
# app.add_url_rule("/<name>", view_func=index(name=name))