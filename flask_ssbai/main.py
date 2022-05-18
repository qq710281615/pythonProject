
from flask import Flask
app = Flask(__name__)

from urls import *


# @app.route("/<name>")
# def index(name):
#     print(uuid.uuid4())
#     print(request)
#     return "thanks  {0};uuid是{1}".format(name, uuid.uuid4())


if __name__ == '__main__':

    app.run(port=6666, debug=True)
