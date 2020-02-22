from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test")
def test():
    return render_template("takeTest.html")


@app.route("/dyslexia")
def dyslexia():
    return render_template("./test/dyslexia.html")


@app.route("/adhd")
def adhd():
    return render_template("./test/adhd.html")


@app.route("/autism")
def autism():
    return render_template("./test/autism.html")


if __name__ == "__main__":
    app.run(debug=True)
    # We made two new changes
