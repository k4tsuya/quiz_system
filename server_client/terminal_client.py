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
        self.question_amount: int = (
            5  # Default number of questions if available
        )
        self.score: int = 0
        self.run_quiz_system()

    def clear_terminal(self) -> None:
        """Clear the terminal screen."""
        cmd = "cls" if os.name == "nt" else "clear"
        subprocess.run(cmd, shell=False, check=True)

    def run_quiz_system(self) -> None:
        """Run the Terminal Quiz Application."""
        commands: dict = {
            "0": exit,
            "1": self.start_quiz,
            "2": self.get_set_topic,
            "3": self.set_difficulty_level,
            "4": self.add_new_topic,
            "5": self.add_new_question,
            "6": self.add_answers_to_question,
            "7": self.delete_question,
        }

        self.clear_terminal()
        while True:
            print("Welcome to the Quiz Application!")
            print("\nPlease select an option:")
            print("-------------------------")
            print("1. Start a new quiz")
            print("2. View and set quiz topic.")
            print("3. Set difficulty level.")
            print("4. Add new topic")
            print("5. Add new question")
            print("6. Add answers to a question")
            print("7. Delete a question")
            print("0. Exit\n")
            choice: str = input("Enter your choice: ")

            commands[choice]()

    def start_quiz(self) -> None:
        """Start a new quiz with the selected difficulty level."""
        self.clear_terminal()
        self.connect_to_db()
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

            print("0. None of the above.\n")
            selected_answer: int = int(
                input("\nEnter your answer by entering the number: "),
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

        if len(questions) > 0:
            print(f"You have {correct} out of {len(questions)} correct.")
            input("Press Enter to exit...")
            self.clear_terminal()
        else:
            print("\nNo questions available for this quiz.")
            input("Press Enter to exit...")
            self.clear_terminal()
        self.close_connection()

    def get_set_topic(self) -> None:
        """Set the topic for the quiz."""
        self.clear_terminal()
        self.connect_to_db()
        set_topic: bool = True
        print("Quiz Topics:\n")
        for item in self.get_topics():
            print(item)

        while set_topic:
            self.topic = input(
                "\nEnter the topic name (case sensitive) to select: ",
            )

            if self.topic not in list(self.get_topics()):
                print("Invalid topic name. Please try again.")
            else:
                print(f"Topic has successfully set to {self.topic}.")
                set_topic: bool = False

        input("Press Enter to start continue...")
        self.clear_terminal()
        self.close_connection()

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

        print("Difficulty level set to: ", self.difficulty_level)
        input("Press Enter to continue...")
        self.clear_terminal()

    def add_new_topic(self) -> None:
        """Add a new topic to the quiz."""
        self.clear_terminal()
        self.connect_to_db()
        adding_topic: bool = True
        while adding_topic:
            print("Adding topic:")
            print("Leave topic blank to exit.\n")
            topic_name = input("Enter the name of the topic: ")
            if not topic_name:
                adding_topic = False
            else:
                self.add_topic(topic_name)
                adding_topic = False
        input("Press Enter to continue...")
        self.clear_terminal()
        self.close_connection()

    def add_new_question(self) -> None:
        """Add a new question to the quiz."""
        self.clear_terminal()
        self.connect_to_db()
        print("Adding question: ")
        print("---------------------")
        topics = self.get_topics()
        adding_question: bool = True
        print(topics)

        topic_name = input(
            "Enter the question's topic name (case sensitive): ",
        )

        while adding_question:
            if not topic_name:
                adding_question = False
            elif topic_name not in topics:
                print(f"Topic '{topic_name}' does not exist.")
                input("Press Enter to continue...")
                self.clear_terminal()
                adding_question = False
            else:
                question = input("Enter the question to add: ")
                if not question:
                    adding_question = False
                else:
                    self.add_question(topic_name, question)
                    print("\nQuestion added successfully.")
                    print("\nPress Enter to continue...")
                    self.clear_terminal()
                    adding_question = False
        self.close_connection()

    def add_answers_to_question(self) -> None:
        """Add answers to a specific question."""
        self.clear_terminal()
        self.connect_to_db()
        adding_answer: bool = True

        sub_command = {
            "1": self.list_all_questions,
            "2": self.add_answers_to_question,
            "3": exit,
        }

        print("Adding answers to a specific question:")
        print("-------------------\n")
        print("1. List all questions")
        print("2. Add answers to a specific question")
        print("3. Exit\n")
        option: str = input("Please select an option: ")
        sub_command[option]()

        while adding_answer:
            question_id = input(
                "\nEnter the id of the question to add answers: ",
            )
            answer: str = input("Enter the answer to add: ")
            is_correct: bool = input(
                "Is the answer correct? (True/False): ",
            )
            if not question_id:
                adding_answer = False
            else:
                self.add_answers(question_id, answer, is_correct)
                adding_answer = False
        print("\nAnswer added successfully.")
        input("Press Enter to continue...")
        self.clear_terminal()
        self.close_connection()

    def list_all_questions(self) -> None:
        """List all questions and its id."""
        self.clear_terminal()
        self.connect_to_db()
        available_questions = self.get_available_questions()
        print("Available Questions:\n")
        for index, question in enumerate(available_questions):
            print(f"{index + 1}. {question['question']}")
        self.close_connection()

    def delete_question(self) -> None:
        """Delete a question."""
        self.connect_to_db()
        self.clear_terminal()
        deleting_question: bool = True

        sub_command = {
            "1": self.list_all_questions,
            "2": self.delete_question_from_db,
            "3": exit,
        }

        print("Deleting question and its answers:")
        print("-------------------\n")
        print("1. List all questions")
        print("2. Delete question with its id.")
        print("3. Exit\n")
        option: str = input("Please select an option: ")
        sub_command[option]()

        print("--------------------\n")

        while deleting_question:
            question_id: int = input(
                "Enter the id of the question you want to delete: ",
            )
            if question_id:
                confirmation = input(
                    "Are you sure you want to delete this question? (y/n): ",
                )
                if confirmation.lower() == "y":
                    self.delete_question_from_db(question_id)
                    print(f"Question with id {question_id} has been deleted.")
                    input("Press Enter to continue...")
                    deleting_question = False
                else:
                    print("\nNo question id provided.")
                    input("Press Enter to continue...")
                    deleting_question = False
        self.close_connection()

    def reset_quiz_db(self) -> str:
        """Reset the quiz database."""
        self.connect_to_db()
        self.purge_quiz_database()
        self.initialize_database_structure()
        self.load_sample_data()
        self.close_connection()
        return "Quiz database has been reset."
