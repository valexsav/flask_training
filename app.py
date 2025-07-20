from flask import Flask

app = Flask(__name__)


@app.route("/index")
def main_page():
    return "<h1>Hi there!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
