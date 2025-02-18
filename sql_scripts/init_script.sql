CREATE TABLE IF NOT EXISTS quiz_topic (
    topic_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS quiz_questions (
    question_id SERIAL PRIMARY KEY,
    topic_name TEXT REFERENCES quiz_topic (name) ON DELETE CASCADE,
    question TEXT NOT NULL


);

CREATE TABLE IF NOT EXISTS quiz_answers (
    answer_id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES quiz_questions (question_id) ON DELETE CASCADE,
    answer TEXT NOT NULL,
    correct BOOLEAN NOT NULL
);