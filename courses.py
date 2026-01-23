import db

def add_course(name, code, grade, credits, user_id):
    sql = "INSERT INTO courses (name, code, grade, credits, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [name, code, grade, credits, user_id])