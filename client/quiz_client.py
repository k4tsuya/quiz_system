"""Quiz Client."""

from sql_client import PostgresqlClient


class QuizClient(PostgresqlClient):
    """Quiz Client class with methods to interact with the quiz database."""

    def __init__(self, host: str, port: int, user: str, password: str) -> None:
        """Initialize the client with database connection details."""
        super().__init__(host, port, user, password)
        self.table_name = "quiz"
        self.difficulty_level = 0

    def initialize_quiz_data(self) -> dict:
        """Initialize quiz data from db."""
        # TODO: Implement initialization logic from db

    # Quiz
    def get_quiz_data(self, quiz_id: int) -> dict:
        """Get quiz data from db."""
        # TODO: Implement logic to get quiz data from db

    def get_random_questions(self, quiz_id: int) -> dict:
        """Get random question from db."""
        # TODO: Implement logic to get random questions from db

    def get_correct_answer(self, quiz_id: int) -> str:
        """Get correct answer from db."""
        # TODO: Implement logic to get correct answer from db

    def set_difficulty_level(
        self,
        quiz_id: int,
        difficulty_level: int,
    ) -> None:
        """Set difficulty level of quiz."""
        # TODO: Implement logic to set difficulty level of quiz

    # Questions
    def add_question(
        self,
        quiz_id: int,
        question: str,
    ) -> None:
        """Add question to db."""
        # TODO: Implement logic to add question to db

    def add_answers(
        self,
        quiz_id: int,
        answers: str,
        correct_answer: str,
    ) -> None:
        """Add answers to db."""
        # TODO: Implement logic to add answers to db

    def update_question(
        self,
        quiz_id: int,
        question: str,
        correct_answer: str,
    ) -> None:
        """Update question in db."""
        # TODO: Implement logic to update question in db

    def delete_question(self, quiz_id: int) -> None:
        """Delete question from db."""
        # TODO: Implement logic to delete question from db

    def add_topic(
        self,
        topic_name: str,
    ) -> None:
        """Add topic to db."""
        # TODO: Implement logic to add topic to db

    # System
    def close_quiz_system(self) -> None:
        """Close quiz system."""
        # TODO: Implement logic to close quiz system
