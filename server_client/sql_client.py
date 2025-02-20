"""PostgreSQL client."""

from dataclasses import dataclass
from pathlib import Path
from typing import Self

import psycopg2


def verify_messenger(function: callable) -> callable:
    """Verify the messenger."""

    def func(self: Self, *args: tuple, **kwargs: dict) -> Self:
        """Verify if the messenger is set before calling the function."""
        try:
            if self.messenger:
                return function(self, *args, **kwargs)

        except ValueError as e:
            print(f"Error: {e}")

    return func


@dataclass
class Configuration:
    """PostgreSQL configuration class."""

    host: str
    port: int
    user: str
    password: str
    dbname: str


class PostgresqlClient:
    """PostgreSQL client class for interacting with PostgreSQL databases."""

    def __init__(self, config: dict, table_name: str) -> None:
        """
        Initialize the PostgreSQL client.

        Args:
            config (dict): Configuration data for the PostgreSQL server.
            table_name (str): The name of the table to be used.

        """
        self.config: Configuration = self.verify_config(config)
        self.table_name = table_name
        self.db_connection = None
        self.messenger = None

    def verify_config(self, config: dict) -> dict:
        """Verify and return the configuration data."""
        return Configuration(**config)

    # Establish a connection
    def connect_to_db(self) -> None:
        """Connect to the PostgreSQL database."""
        try:
            self.db_connection = psycopg2.connect(
                host=self.config.host,
                port=self.config.port,
                user=self.config.user,
                password=self.config.password,
                dbname=self.config.dbname,
            )
            self.messenger = self.db_connection.cursor()

        except psycopg2.OperationalError as e:
            print(f"Error: {e}")

    def initialize_database_structure(self) -> dict:
        """Initialize quiz database structure."""
        with Path.open(
            "./sql_scripts/init_script.sql",
            "r",
        ) as file:
            sql_script = file.read()
            self.messenger.execute(sql_script)
            self.db_connection.commit()
        print("Database structure initialized successfully.")

    def close_connection(self) -> None:
        """Close the database connection."""
        if self.db_connection:
            self.messenger.close()
            self.db_connection.close()
