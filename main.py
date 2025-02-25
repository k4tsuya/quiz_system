"""Main.py for the quiz_system project."""

import os

from dotenv import load_dotenv

from server_client.terminal_client import TerminalClient

load_dotenv()

config_data: dict = {
    "db_host": os.environ.get("DB_HOST"),
    "db_port": os.environ.get("DB_PORT"),
    "db_user": os.environ.get("DB_USER"),
    "db_password": os.environ.get("DB_PASSWORD"),
    "db_name": os.environ.get("DB_NAME"),
}


table_name: str = "quiz"

client = TerminalClient(config_data, table_name)
