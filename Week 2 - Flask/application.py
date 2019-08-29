from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello Flask!"


@app.route("/<string:name>")
def name(name):
    return f"Hello, {name}"


@app.route("/template")
def template():
    name = "Flask"
    condition = name == "Flask"
    return render_template("template.html", name=name, condition=condition)


if __name__ == "__main__":
    app.run(debug=True)
