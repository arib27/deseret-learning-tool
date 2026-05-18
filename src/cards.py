import json
from pathlib import Path

SRC_FOLDER = Path(__file__).resolve().parent  # src/
PROJ_FOLDER = SRC_FOLDER.parent  # project/
DATA_FOLDER = PROJ_FOLDER / "data"  # project/data/
json_path = DATA_FOLDER / "alphabet.json"


# define cards creation
def load_cards(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for d in data:  # reset json data for each session
        d.pop("interval", None)
        d.pop("ease", None)
        d.pop("due", None)

    return [Card.from_dict(d) for d in data]


# create function that saves cards
def save_cards(cards, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in cards], f, indent=4)


# create Card class
class Card:
    def __init__(self, prompt, answer, interval=1, ease=2.5, due=0, **kwargs):
        self.prompt = prompt  # e.g., "𐐀"
        self.answer = answer  # e.g., "a"
        self.interval = interval  # days until next review
        self.ease = ease  # ease factor
        self.due = due  # next due time

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.review_cards = []
        self.current_card_index = 0

    def to_dict(self):
        data = self.__dict__.copy()
        data.pop("review_cards", None)
        data.pop("current_card_index", None)
        return data

    @staticmethod
    def from_dict(data):
        return Card(**data)


# save quality information to card for review session
def update_card(card, quality):
    if quality < 3:
        card.interval = 1
    else:
        card.interval = int(card.interval * card.ease)
        card.ease = max(1.3, card.ease + (0.1 - (5 - quality) * 0.08))

    card.due += card.interval


# find due cards
def get_due_cards(cards, current_day):
    return [c for c in cards if c.due <= current_day]
