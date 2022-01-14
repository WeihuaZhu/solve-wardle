from english_words import english_words_set
import string


def is_word_valid(word):
    a_to_z = set(string.ascii_lowercase)
    for letter in word:
        if letter not in a_to_z:
            return False
    return True


def get_all_5_letter_words():
    words = {word.lower() for word in english_words_set if len(word) == 5}
    words = {word for word in words if is_word_valid(word)}
    return words


res = get_all_5_letter_words()
print(len(res))
