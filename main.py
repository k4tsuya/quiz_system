"""Main.py for the quiz_system project."""

from client import QuizClient

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
client.add_topic("PostgreSQL")

print(client.list_topics())
client.close_connection()
