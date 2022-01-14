from utils import get_all_5_letter_words
import string

ALL_WORDS = frozenset(get_all_5_letter_words())


def get_single_letter_freq_wo_dup():
    count = {x: 0 for x in string.ascii_lowercase}
    for word in ALL_WORDS:
        for letter in set(word):
            letter = letter.lower()
            count[letter] += 1
    return count


count = get_single_letter_freq_wo_dup()
count_tuples = [(k, v) for k, v in count.items()]
count_tuples.sort(key=lambda x: x[1], reverse=True)
print(count_tuples)
