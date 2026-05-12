from pathlib import Path
import json
import random

SRC_FOLDER = Path(__file__).resolve().parent  # src/
PROJ_FOLDER = SRC_FOLDER.parent  # project/
DATA_FOLDER = PROJ_FOLDER / "data"  # project/data/
SPELLING_DATA = DATA_FOLDER / "spelling_book.json"

# issues
# implement spaced repetition
# gotta edit that json more: weird capitalizations, 'and's, strange multiples
# add comment notes to this file

with open(SPELLING_DATA, "r", encoding="utf-8") as file:
    spelling_book = json.load(file)


class TypingPractice:
    def __init__(self, mode="deseret_to_latin", difficulty=1):
        self.current_prompt = None
        self.start_time = None
        self.mode = mode
        self.difficulty = difficulty

        self.word_level = [
            word for word in spelling_book if word["difficulty"] == self.difficulty
        ]

    def join_deseret_multiples(self, entry):
        if isinstance(entry, list):
            return ", ".join(entry)
        return entry

    def next_question(self):
        self.current_prompt = random.choice(self.word_level)

        if self.mode == "latin_to_deseret":
            return self.join_deseret_multiples(self.current_prompt["latin"])
        if self.mode == "deseret_to_latin":
            return self.join_deseret_multiples(self.current_prompt["deseret"])

    def get_answer(self):
        if self.mode == "latin_to_deseret":
            return self.join_deseret_multiples(self.current_prompt["deseret"])
        if self.mode == "deseret_to_latin":
            return self.join_deseret_multiples(self.current_prompt["latin"])

    def grade_answer(self, user_answer):
        if self.mode == "latin_to_deseret":
            correct_answers = self.current_prompt["deseret"]
        elif self.mode == "deseret_to_latin":
            correct_answers = self.current_prompt["latin"]

        user_answer_clean = user_answer.strip()

        if isinstance(correct_answers, list):
            clean_list = [ans.strip() for ans in correct_answers]
            return user_answer_clean in clean_list
        return user_answer_clean == correct_answers.strip()
