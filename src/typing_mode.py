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
    def __init__(self, mode="Latin to Deseret", difficulty=1):
        self.current_prompt = None
        self.start_time = None
        self.mode = mode
        self.difficulty = difficulty

        self.word_level = [
            word for word in spelling_book if word["difficulty"] == self.difficulty
        ]

    def next_question(self):
        self.current_prompt = random.choice(self.word_level)

        if self.mode == "latin to deseret":
            return self.current_prompt["Latin"]
        if self.mode == "deseret to latin":
            return self.current_prompt["Deseret"]

    def get_answer(self):
        if self.mode == "latin to deseret":
            return self.current_prompt["Deseret"]
        if self.mode == "deseret to latin":
            return self.current_prompt["Latin"]

    def grade_answer(self, user_answer):
        correct_answer = self.get_answer()
        return user_answer.strip() == correct_answer.strip()
