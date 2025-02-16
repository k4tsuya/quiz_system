"""Quiz Client."""

from enum import Enum, IntEnum

import psycopg2
import psycopg2.errorcodes

from .sql_client import PostgresqlClient


class TrueFalseBoolean(Enum):
    """Enum for correct answers."""

    CORRECT = True
    INCORRECT = False


class DifficultyLevel(IntEnum):
    """Enum for difficulty levels."""

    EASY = 1
    MEDIUM = 2
    HARD = 3


class QuizClient(PostgresqlClient):
    """Quiz Client class with methods to interact with the quiz database."""

    def __init__(self, config: dict, database: str) -> None:
        """Initialize the quiz client."""
        super().__init__(config, database)

    # Quiz
    def get_available_questions(self) -> list:
        """Get quiz data from db."""
        self.messenger.execute(
            "SELECT question_id, question FROM quiz_questions;",
        )
        question = [x.name for x in self.messenger.description]
        return [dict(zip(question, row)) for row in self.messenger.fetchall()]

    def get_quiz_answers(self) -> list:
        """Get quiz answers from db."""
        self.messenger.execute(
            "SELECT question_id, answer, correct FROM quiz_answers;",
        )
        question = [x.name for x in self.messenger.description]
        return [dict(zip(question, row)) for row in self.messenger.fetchall()]

    def get_random_questions(
        self,
        topic_name: str,
        question_amount: int,
    ) -> list:
        """Get random question from db."""
        self.messenger.execute(
            """
            SELECT question_id, question FROM quiz_questions
            WHERE topic_name = %s
            ORDER BY RANDOM() LIMIT %s;
            """,
            (
                topic_name,
                question_amount,
            ),
        )
        question = [x.name for x in self.messenger.description]

        return [dict(zip(question, row)) for row in self.messenger.fetchall()]

    def get_random_answers(
        self,
        question_id: int,
        difficulty_level: DifficultyLevel,
    ) -> list:
        """Get random answers from db."""
        answer_count = (
            3
            if (difficulty_level == DifficultyLevel.EASY)
            else 4
            if (difficulty_level == DifficultyLevel.MEDIUM)
            else 5
            if (difficulty_level == DifficultyLevel.HARD)
            else None,
        )

        try:
            if (
                difficulty_level >= DifficultyLevel.EASY
                and difficulty_level <= DifficultyLevel.HARD
            ):
                self.messenger.execute(
                    """
                    SELECT question_id, answer_id, answer, correct
                    FROM quiz_answers
                    WHERE question_id = %s ORDER BY RANDOM() LIMIT %s;
                    """,
                    (question_id, answer_count),
                )
                question = [x.name for x in self.messenger.description]
                return [
                    dict(zip(question, row))
                    for row in self.messenger.fetchall()
                ]
            msg = "Difficulty level must be 1, 2 or 3."
            raise ValueError(msg)
        except psycopg2.OperationalError as e:
            print(f"An error occurred: {e}")

    def set_difficulty_level(
        self,
        difficulty_level: int,
    ) -> None:
        """Set difficulty level of quiz."""
        self.difficulty_level = difficulty_level

    # Questions
    def add_question(
        self,
        topic_name: str,
        question: str,
    ) -> None:
        """Add question to db."""
        try:
            self.messenger.execute(
                """
                INSERT INTO quiz_questions (topic_name, question)
                    VALUES (%s, %s);
                    COMMIT;
                    """,
                (topic_name, question),
            )
            print("Question added successfully.")
        except psycopg2.OperationalError as e:
            print(f"Error adding question: {e}")

    def add_answers(
        self,
        question_id: int,
        answer: str,
        correct: TrueFalseBoolean,
    ) -> None:
        """Add answers to db."""
        try:
            self.messenger.execute(
                """INSERT INTO quiz_answers (
                    question_id, answer, correct)
                    VALUES (%s, %s, %s);
                    COMMIT;
                    """,
                (question_id, answer, correct),
            )
            print("Answer added successfully.")
        except psycopg2.OperationalError as e:
            print(f"Error adding question: {e}")

    def update_question(
        self,
        question_id: int,
        question: str,
    ) -> None:
        """Update question in db."""
        try:
            self.messenger.execute(
                """UPDATE quiz_questions SET question = %s
                WHERE question_id = %s;
                """,
                (question, question_id),
            )
            print("Question updated successfully.")
        except psycopg2.OperationalError as e:
            print(f"Error updating question: {e}")

    def delete_question(self, question_id: int) -> None:
        """Delete question from db."""
        try:
            self.messenger.execute(
                """DELETE FROM quiz_questions WHERE question_id = %s;
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
                """INSERT INTO quiz_topic (name)
                    VALUES (%s);
                    COMMIT;
                    """,
                (name,),
            )
            print(f"Added topic: {name}")
        except ValueError as e:
            print(f"Error adding topic: {e}")

    def get_topics(self) -> list[str]:
        """List all topics in db."""
        self.messenger.execute("SELECT name FROM quiz_topic;")
        return [row[0] for row in self.messenger.fetchall()]

    # System
    def purge_quiz_database(self) -> None:
        """Purge quiz database."""
        try:
            self.messenger.execute("""
                DROP SCHEMA public cascade;
                CREATE SCHEMA public;
            """)
        except psycopg2.errors.OperationalError as e:
            print(f"Error purging quiz database: {e}")
        else:
            print("Quiz database purged successfully.")
