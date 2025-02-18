"""Main.py for the quiz_system project."""

from terminal_client import TerminalClient

config_data: dict = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "dbname": "quiz_system",
}

table_name: str = "quiz"

client = TerminalClient(config_data, table_name)


client.connect_to_db()
# client.purge_quiz_database()
# client.initialize_database_structure()
# client.load_sample_data()
client.run_quiz()
client.close_connection()
