import db

def add_course(name, code, grade, credits, user_id):
    sql = "INSERT INTO courses (name, code, grade, credits, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [name, code, grade, credits, user_id])
    
def get_courses():
    sql = "SELECT id, name FROM courses ORDER BY id DESC"
    
    return db.query(sql)

def get_course(course_id):
    sql = """SELECT courses.name,
                    courses.code,
                    courses.grade,
                    courses.credits,
                    users.username
            FROM courses, users
            WHERE courses.user_id = users.id AND
                  courses.id = ?"""
    
    return db.query(sql, [course_id])[0]
