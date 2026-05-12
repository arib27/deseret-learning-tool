import json
from pathlib import Path

SRC_FOLDER = Path(__file__).resolve().parent  # src/
PROJ_FOLDER = SRC_FOLDER.parent  # project/
DATA_FOLDER = PROJ_FOLDER / "data"  # project/data/

## to do


# define cards creation
def load_cards(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Card.from_dict(d) for d in data]


# create Card class
class Card:
    def __init__(self, prompt, answer, interval=1, ease=2.5, due=0):
        self.prompt = prompt  # e.g., "𐐀"
        self.answer = answer  # e.g., "a"
        self.interval = interval  # days until next review
        self.ease = ease  # ease factor
        self.due = due  # next due time (int or timestamp)
        self.review_cards = []
        self.current_card_index = 0

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Card(**data)


def update_card(card, quality):
    if quality < 3:
        card.interval = 1
    else:
        card.interval = int(card.interval * card.ease)
        card.ease = max(1.3, card.ease + (0.1 - (5 - quality) * 0.08))

    card.due += card.interval


def get_due_cards(cards, current_day):
    return [c for c in cards if c.due <= current_day]


def review_session(cards):
    current_day = 0
    due_cards = get_due_cards(cards, current_day)

    for card in due_cards:
        print(card.prompt)
        user_input = input("Answer: ")

        if user_input.strip().lower() == card.answer:
            quality = 5
            print("Correct!")
        else:
            quality = 2
            print(f"Incorrect! Right answer: {card.answer}")

        update_card(card, quality)


json_path = DATA_FOLDER / "alphabet.json"
# cards = load_cards(json_path)
# review_session(cards)
