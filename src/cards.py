import json


# create Card class
class Card:
    def __init__(self):
        self.alphabet_dict = {}
        with open("alphabet.json", "r") as fh:
            self.alphabet_dict = json.load(fh)
