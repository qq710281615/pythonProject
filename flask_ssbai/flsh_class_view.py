
from flask import Flask, request
from flask.views import View
app = Flask(__name__)


class MyView(View):
    methods = ['GET', 'POST']

    def get_met(self):
        print(request)
        print(request.args)
        return "get"

    def dispatch_request(self):
        m = {"GET": self.get_met, "POST": "1"}
        f = m.get(request.method)
        return f()


app.add_url_rule('/', view_func=MyView.as_view("ssbai"))


if __name__ == '__main__':

    app.run(port=6667, debug=True)
