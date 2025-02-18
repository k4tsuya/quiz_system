INSERT INTO quiz_topic (name)
VALUES ('Python'), ('PostgreSQL'),('Geography');

INSERT INTO quiz_questions (topic_name, question)
VALUES ('Python', 'How do you call a function in Python?'),
    ('PostgreSQL', 'What is the SQL command to create a table?'),
    ('Geography', 'What is the capital of France?');

INSERT INTO quiz_answers (question_id, answer, correct)
VALUES (1, 'def my_function():', True),
    (1, 'def my_function{}:', False),
    (1, 'def my_function[]:', False),
    (1, 'def my_function<>:', False),

    (2, 'CREATE TABLE my_table', True),
    (3, 'Paris', True);