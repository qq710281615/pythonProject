from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    with open(r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\report\2022-06-02\index.html") as f:
        cont = f.read()
    return cont


if __name__ == '__main__':
    app.run()
