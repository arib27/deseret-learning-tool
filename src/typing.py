from pathlib import Path
import json
import random

SRC_FOLDER = Path(__file__).resolve().parent  # src/
PROJ_FOLDER = SRC_FOLDER.parent  # project/
DATA_FOLDER = PROJ_FOLDER / "data"  # project/data/
SPELLING_DATA = DATA_FOLDER / "spelling_book.json"

with open(SPELLING_DATA, "r", encoding="utf-8") as file:
    spelling_book = json.load(file)


class TypingPractice:
    def __init__(self):
        self.current_prompt = None
        self.start_time = None

        easy_words = [word for word in spelling_book if word["difficulty"] == 1]
        medium_words = [word for word in spelling_book if word["difficulty"] == 2]
        hard_words = [word for word in spelling_book if word["difficulty"] == 3]

    def next_question(self):
        self.current_prompt = random.choice(self.pairs)
        return self.current_prompt

    def grade_answer(self, user_answer):
        correct_answer = self.current_prompt["deseret"]
        user_correct = user_answer == correct_answer
