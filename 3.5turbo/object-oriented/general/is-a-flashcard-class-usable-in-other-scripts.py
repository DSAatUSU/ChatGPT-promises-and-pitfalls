import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"

    def ask_question(self):
        user_input = input(f"{self.question}: ")
        if user_input.lower() == self.answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {self.answer}")

    @staticmethod
    def quiz_flashcards(flashcards):
        random.shuffle(flashcards)
        for flashcard in flashcards:
            flashcard.ask_question()

# Example usage
flashcards = [
    Flashcard("What is the capital of France?", "Paris"),
    Flashcard("What is the largest planet in our solar system?", "Jupiter"),
    Flashcard("What is the symbol for the element gold?", "Au")
]

Flashcard.quiz_flashcards(flashcards)
