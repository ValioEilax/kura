import db

def add_course(name, code, grade, credits, user_id, classes):
    sql = "INSERT INTO courses (name, code, grade, credits, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [name, code, grade, credits, user_id])

    course_id = db.last_insert_id()

    sql = "INSERT INTO course_classes (course_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [course_id, title, value])


def get_courses():
    sql = """
        SELECT courses.id, courses.name, courses.code, courses.credits, users.username, user_id
        FROM courses
        JOIN users ON courses.user_id = users.id
        ORDER BY courses.id DESC
    """
    return db.query(sql)


def get_course(course_id):
    sql = """SELECT courses.id,
                    courses.name,
                    courses.code,
                    courses.grade,
                    courses.credits,
                    users.id user_id,
                    users.username
            FROM courses, users
            WHERE courses.user_id = users.id AND
                  courses.id = ?"""

    result = db.query(sql, [course_id])
    return result[0] if result else None

def get_review(course_id):
    sql = """
    SELECT r.id, r.course_id, r.rating, c.name
    FROM reviews r
    JOIN courses c ON c.id = r.course_id
    WHERE r.course_id = ?
    """

    result = db.query(sql, [course_id])
    return result[0] if result else None


def get_classes(course_id):
    sql = "SELECT title, value FROM course_classes WHERE course_id = ?"
    return db.query(sql, [course_id])


def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes


def update_course(course_id, name, code, grade, credits, classes):
    sql = """UPDATE courses
             SET name = ?, code = ?, grade = ?, credits = ?
             WHERE id = ?"""
    db.execute(sql, [name, code, grade, credits, course_id])

    sql = "DELETE FROM course_classes WHERE course_id = ?"
    db.execute(sql, [course_id])

    sql = "INSERT INTO course_classes (course_id, title, value)VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [course_id, title, value])


def remove_course(course_id):
    sql = "DELETE FROM courses WHERE id = ?"
    db.execute(sql, [course_id])


def find_courses(query):
    sql = """
    SELECT c.id, c.name, c.code, c.user_id, c.credits, u.username
    FROM courses c
    JOIN users u ON c.user_id = u.id
    WHERE c.name LIKE ? OR c.code LIKE ? OR u.username LIKE ?
    ORDER BY c.id DESC
    """

    pattern = "%" + query + "%"
    return db.query(sql, [pattern, pattern, pattern])
