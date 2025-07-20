from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/index")
def main_page():
    return render_template("index.html")

@app.route("/")
def redirect_to_main_page():
    return redirect(url_for("main_page"))

if __name__ == "__main__":
    app.run(debug=True)
