from flask import Flask, request, render_template

from Functions.password import user_check

app = Flask(__name__)

#count for get requests
get_count = 0

@app.route("/", methods=["GET"])
def start():

    if request.method == "GET":
        return render_template("about_us.html")
    
@app.route("/login", methods =["GET", "POST"])
def login():
    global get_count
    if get_count > 0:
        return render_template("index.html")
    
    if request.method == "GET":
        return render_template("Login_Page.html")
    
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("pass")

        state = user_check(name, password)

        if state:
            get_count += 1
            return render_template("index.html")

        return render_template("Login_Page.html", Message = "Invalid Entry")
    
    