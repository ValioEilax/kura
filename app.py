import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
import config
import db, courses, reviews

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    all_courses = courses.get_courses()
    all_reviews = reviews.get_reviews()
    return render_template("index.html", courses=all_courses, reviews=all_reviews)

@app.route("/find_course")
def find_course():
    query = request.args.get("query")
    if query:
        results = courses.find_courses(query)
    else:
        query = ""
        results = []
    return render_template("find_course.html", query=query, results=results)

@app.route("/course/<int:course_id>")
def show_course(course_id):
    course = courses.get_course(course_id)
    return render_template("show_course.html", course=course)

@app.route("/new_course")
def new_course():
    return render_template("new_course.html")

@app.route("/create_course", methods=["POST"])
def create_course():
    name = request.form["name"]
    code = request.form["code"]
    credits = request.form["credits"]
    grade = request.form["grade"]
    user_id = session["user_id"]
    
    courses.add_course(name, code, grade, credits, user_id)
    
    return redirect("/")

@app.route("/update_course", methods=["POST"])
def update_course():
    course_id = request.form["course_id"]
    course = courses.get_course(course_id)
    if course["user_id"] != session["user_id"]:
        abort(403)
    
    name = request.form["name"]
    code = request.form["code"]
    credits = request.form["credits"]
    grade = request.form["grade"]
    user_id = session["user_id"]
    
    courses.update_course(course_id, name, code, grade, credits)
    
    return redirect("/course/" + str(course_id))

@app.route("/edit_course/<int:course_id>")
def edit_course(course_id):
    course = courses.get_course(course_id)
    if course["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_course.html", course=course)

@app.route("/remove_course/<int:course_id>", methods=["GET", "POST"])
def remove_course(course_id):
    course = courses.get_course(course_id)
    if course["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_course.html", course=course)
    
    if request.method == "POST":
        if "remove" in request.form:
            courses.remove_course(course_id)
            return redirect("/")
        else:
            return redirect("/course/" + str(course_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: salasanat eivät täsmää")
        return render_template("register.html")
    password_hash = generate_password_hash(password1)
    
    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        flash("VIRHE: Valitsemasi tunnus on jo varattu")
        return render_template("register.html")
    
    flash("Tunnus luotu onnistuneesti! Voit nyt kirjautua sisään.")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:            
            flash("VIRHE: väärä tunnus tai salasana")
            return render_template("login.html")
        
@app.route("/my_courses")

@app.route("/course/<int:course_id>/new_review")
def new_review(course_id):
    course = courses.get_course(course_id)
    return render_template("new_review.html", course=course)

@app.route("/course/<int:course_id>/create_review", methods=["POST"])
def create_review(course_id):
    difficulty = request.form["difficulty"]
    workload = request.form["workload"]
    grade = request.form["grade"]
    feedback = request.form["feedback"]
    user_id = session["user_id"]
    
    if reviews.user_has_reviewed(course_id, user_id):
        flash("Olet jo jättänyt palautteen tälle kurssille.", "error")
        return redirect("/course/" + str(course_id))
    
    reviews.add_review(course_id, user_id, difficulty, workload, grade, feedback)
    
    flash("Arvostelu lisätty onnistuneesti!", "success")
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
        
