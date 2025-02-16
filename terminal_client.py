"""Terminal for the quiz application."""

import enum
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

    def clear_terminal(self) -> None:
        """Clear the terminal screen."""
        cmd = "cls" if os.name == "nt" else "clear"
        subprocess.run(cmd, shell=False, check=True)

    def run_quiz(self) -> None:
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

        self.clear_terminal()
        while True:
            print("Welcome to the Quiz Application!")
            print("\nPlease select an option:")
            print("-------------------------")
            print("1. Start a new quiz")
            print("2. View and set quiz topic.")
            print("3. Set difficulty level.")
            print("4. Exit\n")
            choice: str = input("Enter your choice: ")

            commands[choice]()

    def start_quiz(self) -> None:
        """Start a new quiz with the selected difficulty level."""
        # Implement the logic to start a new quiz
        self.clear_terminal()
        questions: list = self.get_random_questions(
            self.topic,
            self.question_amount,
        )

        correct: int = 0

        for question_no, item in enumerate(questions):
            print(f"Question {question_no + 1}: {item['question']}")
            print("--------------------------\n")
            answers: list = self.get_random_answers(
                item["question_id"],
                self.difficulty,
            )

            answer_values: list = []

            for index, answer in enumerate(answers):
                answer_values.append(answer["correct"])
                print(f"{index + 1}. {answer['answer']}")

            print("\nEnter your answer by entering the number: ")
            selected_answer: int = int(
                input("If the correct answer is not in the list enter 0: "),
            )

            if answer_values[selected_answer - 1] is True:
                correct += 1
                print("\nCorrect Answer!")
            elif (selected_answer - 1) == -1:
                if True not in answer_values:
                    correct += 1
                    print("\nCorrect answer!")
            else:
                print("\nIncorrect Answer!")

            input("Press Enter to continue...")
            self.clear_terminal()

        print(f"You have {correct} out of {len(questions)} correct.")
        input("Press Enter to exit...")
        self.clear_terminal()

    def get_set_topic(self) -> None:
        """Set the topic for the quiz."""
        self.clear_terminal()
        set_topic: bool = True
        print("Quiz Topics:\n")
        for item in self.get_topics():
            print(item)

        while set_topic:
            self.topic = input(
                "\nEnter the topic name to select: ",
            )

            if self.topic not in list(self.get_topics()):
                print("Invalid topic name. Please try again.")
            else:
                print(f"Topic has successfully set to {self.topic}.")
                set_topic: bool = False

        input("Press Enter to start continue...")
        self.clear_terminal()

    def set_difficulty_level(self) -> int:
        """Set the difficulty level for the quiz."""
        select_difficulty: bool = True

        while select_difficulty:
            print("Select difficulty level:\n")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")

            choice = input("\nEnter your choice: ")
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
        self.clear_terminal()
