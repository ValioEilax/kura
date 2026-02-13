import db

def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    
    result = db.query(sql, [user_id])
    return result[0] if result else None
    
    
    
def get_courses(user_id):
    sql = "SELECT id, name, code FROM courses WHERE user_id = ?"
    return db.query(sql, [user_id])