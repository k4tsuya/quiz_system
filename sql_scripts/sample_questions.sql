INSERT INTO quiz_topic (name)
VALUES ('Python'), ('PostgreSQL'),('Geography');

INSERT INTO quiz_questions (topic_name, question)
VALUES ('Python', 'How do you call a function in Python?'),
    ('PostgreSQL', 'What is the SQL command to create a table?'),
    ('Geography', 'What is the capital of France?'),
    ('Python', 'What is the difference between a list and a tuple');

INSERT INTO quiz_answers (question_id, answer, correct)
VALUES (1, 'def my_function():', True),
    (1, 'def my_function{}:', False),
    (1, 'def my_function[]:', False),
    (1, 'def my_function<>:', False),

    (2, 'CREATE TABLE my_table', True),
    (3, 'Paris', True),
    (4, 'Lists are mutable and tuples are immutable.', True),
    (4, 'Tuples are mutable and lists are immutable.', False),
    (4, 'Lists and tuples are both mutable.', False),
    (4, 'Lists and tuples are both immutable', False)
    ;