from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index5.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        if name == "":
            return "Please enter a valid input"
        else:
            return render_template("hello.html",name = name)
