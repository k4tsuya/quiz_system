"""Quiz Client."""

import psycopg2
import psycopg2.errorcodes

from .sql_client import PostgresqlClient


class QuizClient(PostgresqlClient):
    """Quiz Client class with methods to interact with the quiz database."""

    def __init__(self, config: dict, database: str) -> None:
        """Initialize the quiz client."""
        super().__init__(config, database)
        self.difficulty_level = 0

    # Quiz
    def get_available_questions(self) -> list:
        """Get quiz data from db."""
        self.messenger.execute("SELECT question FROM questions;")
        return [row[0] for row in self.messenger.fetchall()]

    def get_random_questions(self, quiz_id: int) -> dict:
        """Get random question from db."""
        # TODO: Implement logic to get random questions from db

    def set_difficulty_level(
        self,
        difficulty_level: int,
    ) -> None:
        """Set difficulty level of quiz."""
        self.difficulty_level = difficulty_level

    # Questions
    def add_question(
        self,
        topic: str,
        question: str,
    ) -> None:
        """Add question to db."""
        try:
            self.messenger.execute(
                """INSERT INTO questions (topic, question)
            VALUES (%s, %s);
            COMMIT;
            """,
                (topic, question),
            )
        except psycopg2.OperationalError as e:
            print(f"Error adding question: {e}")

    def add_answers(
        self,
        quiz_id: int,
        answers: str,
        correct_answer: str,
    ) -> None:
        """Add answers to db."""
        # TODO: Implement logic to add answers to db

    # OPTIONAL
    def update_question(
        self,
        quiz_id: int,
        question: str,
        correct_answer: str,
    ) -> None:
        """Update question in db."""
        # TODO: Implement logic to update question in db

    def delete_question(self, question_id: int) -> None:
        """Delete question from db."""
        try:
            self.messenger.execute(
                """
                DELETE FROM questions WHERE question_id = %s;
                """,
                (question_id,),
            )
            print(
                f"Successfully deleted question with id: {question_id}",
            )
        except psycopg2.OperationalError as e:
            print(f"Error deleting question: {e}")

    def add_topic(self, name: str) -> None:
        """Add topic to db."""
        try:
            self.messenger.execute(
                """
                INSERT INTO quiz_topic (name)
                VALUES (%s);
                COMMIT;
                """,
                (name,),
            )
            print(f"Added topic: {name}")
        except ValueError as e:
            print(f"Error adding topic: {e}")

    def list_topics(self) -> list[str]:
        """List all topics in db."""
        self.messenger.execute("SELECT name FROM quiz_topic;")
        return [row[0] for row in self.messenger.fetchall()]

    # System
    def purge_quiz_database(self) -> None:
        """Purge quiz database."""
        try:
            self.insert_modify_data("""
                DROP SCHEMA public cascade;
                CREATE SCHEMA public;
            """)
        except psycopg2.errors.OperationalError as e:
            print(f"Error purging quiz database: {e}")
        else:
            print("Quiz database purged successfully.")

    def close_quiz_system(self) -> None:
        """Close quiz system."""
