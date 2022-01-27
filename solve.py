from enum import Enum
from collections import namedtuple
import string
from utils import get_all_5_letter_words

Evidence = namedtuple("Evidence", "letter signal position")
ALL_WORDS = frozenset(get_all_5_letter_words())


class Signal(Enum):
    UNKNOWN = 0
    GRAY = 1
    YELLOW = 2
    GREEN = 3


class Strategy:
    def __init__(self):
        self.num_tries = 0
        a_to_z = string.ascii_lowercase
        self.word_choices = list(get_all_5_letter_words())

    def exclude_word_choices(self, new_evidence):
        letter = new_evidence.letter
        signal = new_evidence.signal
        position = new_evidence.position
        if signal == Signal.GRAY:
            filtered = filter(lambda x: letter not in x, self.word_choices)
        elif signal == Signal.YELLOW:
            filtered = filter(
                lambda x: letter in x and x[position] != letter, self.word_choices
            )
        elif signal == Signal.GREEN:
            filtered = filter(lambda x: x[position] == letter, self.word_choices)
        else:
            raise Exception("Invalid evidence")
        self.word_choices = list(filtered)

    def merge_evidence(self, new_evidences):
        for new_evidence in new_evidences:
            self.exclude_word_choices(new_evidence)


def main():
    strategy = Strategy()
    print(strategy.word_choices)


if __name__ == "__main__":
    main()
