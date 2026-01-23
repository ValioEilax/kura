CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
)

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    code TEXT,
    credits INTEGER,
    grade INTEGER
) 

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    difficulty INTEGER,
    workload INTEGER,
    grade INTEGER,
    feedback TEXT
)