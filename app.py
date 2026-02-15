import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session, flash, abort
import config
import db, courses, reviews, users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_courses = courses.get_courses()
    all_reviews = reviews.get_reviews()
    return render_template("index.html", courses=all_courses, reviews=all_reviews)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    courses = users.get_courses(user_id)
    return render_template("show_user.html", user=user, courses=courses)

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
    if not course:
        abort(404)
    classes = courses.get_classes(course_id)
    return render_template("show_course.html", course=course, classes=classes)

@app.route("/new_course")
def new_course():
    require_login()
    
    classes = courses.get_all_classes()
    return render_template("new_course.html", classes=classes)

@app.route("/create_course", methods=["POST"])
def create_course():
    require_login()
    
    name = request.form["name"]
    if not name or len(name) > 50: 
        abort(403)
    code = request.form["code"]
    credits = request.form["credits"]
    grade = request.form["grade"]
    user_id = session["user_id"]
    
    all_classes = courses.get_all_classes()
    
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            title, value = entry.split(":")
            if title not in all_classes:
                abort(403)
            if value not in all_classes[title]:
                abort(403)
            classes.append((title, value))

    courses.add_course(name, code, grade, credits, user_id, classes)
    
    return redirect("/")
    

@app.route("/update_course", methods=["POST"])
def update_course():
    require_login()
    
    course_id = request.form["course_id"]
    course = courses.get_course(course_id)
    if not course:
        abort(404)
    if course["user_id"] != session["user_id"]:
        abort(403)
        
    name = request.form["name"]
    code = request.form["code"]
    credits = request.form["credits"]
    grade = request.form["grade"]
    user_id = session["user_id"]
    
    all_classes = courses.get_all_classes()
    
    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            title, value = entry.split(":")
            if title not in all_classes:
                abort(403)
            if value not in all_classes[title]:
                abort(403)
            classes.append((title, value))

    
    courses.update_course(course_id, name, code, grade, credits, classes)
    
    return redirect("/course/" + str(course_id))

@app.route("/edit_course/<int:course_id>")
def edit_course(course_id):
    require_login()
    
    course = courses.get_course(course_id)
    if not course:
        abort(404)
    if course["user_id"] != session["user_id"]:
        abort(403)
        
    all_classes = courses.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in courses.get_classes(course_id):
        classes[entry["title"]] = entry["value"]
        
    return render_template("edit_course.html", course=course, classes=classes, all_classes=all_classes)

@app.route("/remove_course/<int:course_id>", methods=["GET", "POST"])
def remove_course(course_id):
    require_login()
    
    course = courses.get_course(course_id)
    if not course:
        abort(404)
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
    
    try:
        users.create_user(username, password1)
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
        
        user_id = users.check_login(username, password)
        if user_id:
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
    require_login()

    difficulty = request.form["difficulty"]
    workload = request.form["workload"]
    rating = request.form["rating"]
    feedback = request.form["feedback"]
    user_id = session["user_id"]
    
    if reviews.user_has_reviewed(course_id, user_id):
        flash("Olet jo jättänyt palautteen tälle kurssille.", "error")
        return redirect("/course/" + str(course_id))
    
    reviews.add_review(course_id, user_id, difficulty, workload, rating, feedback)
    
    flash("Arvostelu lisätty onnistuneesti!", "success")
    return redirect("/")


@app.route("/course/<int:course_id>/show_review")
def show_review(course_id):
    review = reviews.get_review(course_id)
    if not review:
        abort(404)
        
    comments = reviews.get_comments(review["id"])
    
    return render_template("show_review.html", review=review, comments=comments)

@app.route("/remove_review/<int:review_id>", methods=["GET", "POST"])
def remove_review(review_id):
    require_login()
    review = reviews.get_review_by_id(review_id)
    if not review:
        abort(404)
    if review["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_review.html", review=review)


    if "remove" in request.form:
        reviews.remove_review(review_id)
        flash("Kurssin arvostelu poistettu onnistuneesti!", "success")

    return redirect(f"/course/{review['course_id']}")


@app.route("/edit_review/<int:review_id>")
def edit_review(review_id):
    require_login()
    
    review = reviews.get_review_by_id(review_id)
    if not review:
        abort(404)
    if review["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_review.html", review=review)

@app.route("/update_review", methods=["POST"])
def update_review():
    require_login()
    
    review_id = request.form["review_id"]
    print(review_id)
    review = reviews.get_review_by_id(review_id)
    if not review:
        abort(404)
    if review["user_id"] != session["user_id"]:
        abort(403)
        
    difficulty = request.form["difficulty"]
    workload = request.form["workload"]
    rating = request.form["rating"]
    feedback = request.form["feedback"]
    
    reviews.update_review(review_id, difficulty, workload, rating, feedback)
    
    flash("Kurssin arvostelua muokattu onnistuneesti!", "sucess")
    return redirect("/course/" + str(review["course_id"]) + "/show_review")

@app.route("/review/<int:review_id>/comment", methods=["POST"])
def add_comment(review_id):
    require_login()
    review = reviews.get_review_by_id(review_id)
    
    content = request.form["content"].strip()
    
    if not content:
        flash("Kommentti ei voi olla tyhjä")
    elif len(content) > 500:
        flash("Kommentti on liian pitkä (max 500 merkkiä)")
    else:
        reviews.add_comment(review_id, session["user_id"], content)
        flash("Kommentti lisätty!")
        
    return redirect("/course/" + str(review["course_id"]) + "/show_review")

@app.route("/comment/<int:comment_id>/delete", methods=["POST"])
def delete_comment(comment_id):
    require_login()

    comment = reviews.get_comment_by_id(comment_id)

    if not comment:
        abort(404)

    if comment["user_id"] != session["user_id"]:
        abort(403)

    review = reviews.get_review_by_id(comment["review_id"])

    reviews.remove_comment(comment_id, session["user_id"])
    flash("Kommentti poistettu.")
        
    return redirect("/course/" + str(review["course_id"]) + "/show_review")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
        
