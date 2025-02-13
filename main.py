"""Main.py for the quiz_system project."""

from client import QuizClient
from client.quiz_client import DifficultyLevel

config_data: dict = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "dbname": "quiz_system",
}

table_name: str = "quiz"

client = QuizClient(config_data, table_name)


client.connect_to_db()
# client.purge_quiz_database()
# client.initialize_database_structure()
# client.add_topic("Python")
# client.add_topic("PostgreSQL")

# print(client.list_topics())

# client.add_question(
#     "Python",
#     "How do you call a function in Python?",
# )
# client.add_answers(1, "function_name()", True)
# client.add_answers(1, "function_name", False)
# client.add_answers(1, "function_name[]", False)
# client.add_answers(1, "function_name{}", False)
# client.add_answers(1, "function_name<>", False)

# client.add_question(
#     "Python",
#     "What is the difference between a list and a tuple?",
# )
# client.add_answers(2, "List is mutable and tuple is immutable.", True)
# client.add_answers(2, "List is immutable and tuple is mutable.", False)
# client.add_answers(2, "List is immutable and tuple is immutable.", False)
# client.add_answers(2, "List is mutable and tuple is mutable.", False)
# client.add_answers(2, "List is immutable and tuple is mutable.", False)


print("\n")
print(client.get_random_answers(1, 1))
# print(client.get_random_questions("Python"))
print("\n")

# client.update_question(1, "How to call a function in Python?")

# print(client.get_available_questions())
# print(client.get_quiz_answers())
# client.delete_question(1)

client.close_connection()
