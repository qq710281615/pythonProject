from flask import Flask

app = Flask(__name__, static_folder="allure_report", static_url_path="/report")


@app.route("/")
def index():
    return "可以访问"


if __name__ == '__main__':
    app.run(debug=True)
