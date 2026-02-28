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
            c.idAS course_id, c.name AS course_name,
            u.id AS user_id, u.username AS reviewer_name
    FROM reviews r
    JOIN courses c ON c.id = r.course_id
    JOIN users u ON u.id = r.user_id
    WHERE r.course_id = ?
    ORDER BY r.created_at DESC
    """

    result = db.query(sql, [course_id])
    return result[0] if result else None


def get_review_by_id(review_id):
    sql = """
    SELECT r.id, r.course_id, r.user_id,
            r.difficulty, r.workload, r.rating, r.feedback, r.created_at,
            c.name AS course_name
    FROM reviews r
    JOIN courses c ON c.id = r.course_id
    WHERE r.id = ?
    """

    result = db.query(sql, [review_id])
    return result[0] if result else None


def remove_review(review_id):
    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])   


def update_review(review_id, difficulty, workload, rating, feedback):
    sql = """
    UPDATE reviews
    SET difficulty = ?, workload = ?, rating = ?, feedback = ?
    WHERE id = ?
    """

    db.execute(sql, [difficulty, workload, rating, feedback, review_id])


def add_comment(review_id, user_id, content):
    sql = "INSERT INTO comments (review_id, user_id, content) VALUES (?, ?, ?)"
    db.execute(sql, [review_id, user_id, content])


def get_comments(review_id):
    sql = """
    SELECT c.id, c.content, c.created_at, c.user_id, u.username 
    FROM comments c 
    JOIN users u ON c.user_id = u.id 
    WHERE c.review_id = ? 
    ORDER BY c.created_at ASC
    """

    return db.query(sql, [review_id])


def get_comment_by_id(comment_id):
    sql = "SELECT id, review_id, user_id, content FROM comments WHERE id = ?"
    result = db.query(sql, [comment_id])
    return result[0] if result else None


def remove_comment(comment_id, user_id):
    sql = "DELETE FROM comments WHERE id = ? AND user_id = ?"
    db.execute(sql, [comment_id, user_id])
