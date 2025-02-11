CREATE TABLE IF NOT EXISTS quiz_topic (
    topic_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS quiz (
    quiz_id  SERIAL PRIMARY KEY,
    module VARCHAR(100) NOT NULL,
    submodule VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS quiz_answers (
    answer_id INTEGER REFERENCES quiz (quiz_id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    correct BOOLEAN NOT NULL
);