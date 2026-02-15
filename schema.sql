CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    code TEXT,
    credits INTEGER,
    grade INTEGER,
    user_id INTEGER REFERENCES users
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id),
    difficulty INTEGER NOT NULL CHECK(difficulty BETWEEN 1 AND 5),
    workload INTEGER NOT NULL CHECK(workload BETWEEN 1 AND 112),
    rating INTEGER NOT NULL CHECK(rating BETWEEN 0 AND 5),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE course_classes (
    id INTEGER PRIMARY KEY,
    course_id INTEGER REFERENCES courses,
    title TEXT,
    value TEXT
);