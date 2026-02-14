import db

def user_has_reviewed(course_id, user_id):
    rows = db.query(
        "SELECT 1 FROM reviews WHERE course_id = ? AND user_id = ? LIMIT 1",
        [course_id, user_id]
    )
    
    return len(rows) > 0
    

def add_review(course_id, user_id, difficulty, workload, rating, feedback):
    sql = "INSERT INTO reviews (course_id, user_id, difficulty, workload, rating, feedback) VALUES (?, ?, ?, ?, ?, ?)"
    db.execute(sql, [course_id, user_id, difficulty, workload, rating, feedback])
    
def get_reviews():
    sql = """
        SELECT r.id, r.rating,
             r.created_at,
             c.id AS course_id, c.name AS course_name,
             u.id AS user_id, u.username AS reviewer_name
        FROM reviews r
        JOIN courses c ON c.id = r.course_id
        JOIN users u ON u.id = r.user_id
        ORDER BY r.created_at DESC
    """
    return db.query(sql)

def get_review(course_id):
    sql = """
        SELECT r.id, r.difficulty, r.workload, r.rating, r.feedback,
             r.created_at,
             c.id AS course_id, c.name AS course_name,
             u.id AS user_id, u.username AS reviewer_name
        FROM reviews r
        JOIN courses c ON c.id = r.course_id
        JOIN users u ON u.id = r.user_id
        WHERE r.course_id = ?
        ORDER BY r.created_at DESC"""
    
    result = db.query(sql, [course_id])
    return result[0] if result else None