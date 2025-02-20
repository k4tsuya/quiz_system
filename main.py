"""Main.py for the quiz_system project."""

from server_client.terminal_client import TerminalClient

config_data: dict = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "dbname": "quiz_system",
}

table_name: str = "quiz"

client = TerminalClient(config_data, table_name)
