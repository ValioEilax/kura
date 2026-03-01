import sqlite3
import random
import time

def fill():

    db = sqlite3.connect("database.db")


    db.execute("PRAGMA synchronous = OFF")
    db.execute("PRAGMA journal_mode = MEMORY")

    print("Clearing old data...")
    db.execute("DELETE FROM comments")
    db.execute("DELETE FROM reviews")
    db.execute("DELETE FROM courses")
    db.execute("DELETE FROM users")

    user_count = 1000
    course_count = 10**5    # 100,000 courses
    review_count = 10**5    # 100,000 reviews
    comment_count = 10**6   # 1,000,000 comments

    start_time = time.time()

    # 1. Create Users
    print(f"Creating {user_count} users...")
    users = []
    for i in range(1, user_count + 1):
        users.append((f"user{i}", "password123"))


    db.executemany("INSERT INTO users (username, password_hash) VALUES (?, ?)", users)

    # 2. Create Courses
    print(f"Creating {course_count} courses...")
    courses_list = []
    for i in range(1, course_count + 1):
        # Format: (name, code, grade, credits, user_id) -> 5 values
        courses_list.append((f"Course {i}", f"TKT{i}", 3, 5, random.randint(1, user_count)))

        if i % 10000 == 0:

            db.executemany("INSERT INTO courses (name, code, grade, credits, user_id) VALUES (?, ?, ?, ?, ?)", courses_list)
            courses_list = []
            print(f" Progress: {i}/{course_count}", end="\r")

    # 3. Create Reviews
    print(f"\nCreating {review_count} reviews...")
    reviews_list = []
    for i in range(1, review_count + 1):
        reviews_list.append((
            i,
            random.randint(1, user_count),
            random.randint(1, 5),
            random.randint(1, 20),
            random.randint(1, 5),
            f"Review for course {i}"
        ))

        if i % 10000 == 0:

            db.executemany("""INSERT INTO reviews (course_id,user_id, difficulty, workload, rating, feedback)
                              VALUES (?, ?, ?, ?, ?, ?)""",reviews_list)
            reviews_list = []
            print(f" Progress: {i}/{review_count}", end="\r")

    # 4. Create Comments
    print(f"\nCreating {comment_count} comments...")
    comments_list = []
    for i in range(1, comment_count + 1):
        comments_list.append((
            random.randint(1, review_count),
            random.randint(1, user_count),
            f"Comment number {i}"
        ))

        if i % 25000 == 0:

            db.executemany("INSERT INTO comments (review_id, user_id, content) VALUES (?, ?, ?)", comments_list)
            comments_list = []
            print(f" Progress: {i}/{comment_count}", end="\r")

    db.commit()
    db.close()

    end_time = time.time()
    print(f"\n\nDone! Total time: {end_time - start_time:.2f}seconds.")

if __name__ == "__main__":
    fill()
