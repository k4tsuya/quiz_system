CREATE TABLE IF NOT EXISTS quiz_topic (
    topic_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS quiz_questions (
    question_id SERIAL PRIMARY KEY,
    topic TEXT REFERENCES quiz_topic (name),
    question TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS quiz_answers (
    question_id INTEGER REFERENCES quiz_questions (question_id),
    answer TEXT NOT NULL,
    correct BOOLEAN NOT NULL
);