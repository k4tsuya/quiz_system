"""Terminal for the quiz application."""

import os
import subprocess

from server_client import QuizClient
from server_client.quiz_client import DifficultyLevel


class TerminalClient(QuizClient):
    """Terminal for the quiz application."""

    def __init__(self, config: dict, database: str) -> None:
        """Initialize the Terminal Quiz Application."""
        super().__init__(config, database)
        self.difficulty: int = DifficultyLevel.EASY  # Default difficulty level
        self.topic: str = "Python"  # Default topic name
        self.question_amount: int = 5  # Default number of questions
        self.score: int = 0

    def clear(self) -> None:
        """Clear the terminal screen."""
        cmd = "cls" if os.name == "nt" else "clear"
        subprocess.run(cmd, shell=False, check=True)

    def run(self) -> None:
        """Run the Terminal Quiz Application."""
        commands: dict = {
            "1": self.start_quiz,
            "2": self.get_set_topic,
            "3": self.set_difficulty_level,
            "4": exit,
            # "4": self.add_new_topic,
            # "5": self.add_new_question,
            # "6": self.update_existing_question,
            # "7": self.delete_question,
        }

        while True:
            print("Welcome to the Quiz Application!")
            print("1. Start a new quiz")
            print("2. View and set quiz topic.")
            print("3. Set difficulty level.")
            print("4. Exit")
            choice: str = input("Enter your choice: ")

            commands[choice]()

    def start_quiz(self) -> None:
        """Start a new quiz with the selected difficulty level."""
        # Implement the logic to start a new quiz
        print("running quiz...")

        questions: list[str] = self.get_random_questions(
            self.topic,
            self.question_amount,
        )

        for question_id, question in questions:
            print(question_id, question)

    def get_set_topic(self) -> None:
        """Set the topic for the quiz."""
        self.clear()
        print("Quiz Topics:\n")
        for item in self.get_topics():
            print(item)

        self.topic = input("\nEnter the topic name to select: ")

    def set_difficulty_level(self) -> int:
        """Set the difficulty level for the quiz."""
        select_difficulty: bool = True

        while select_difficulty:
            print("Select difficulty level:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.difficulty_level = DifficultyLevel.EASY
                select_difficulty: bool = False

            elif choice == "2":
                self.difficulty_level = DifficultyLevel.MEDIUM
                select_difficulty: bool = False

            elif choice == "3":
                self.difficulty_level = DifficultyLevel.HARD
                select_difficulty: bool = False

        print("Difficulty level set to:", self.difficulty_level)
        input("Press Enter to continue...")
        self.clear()
