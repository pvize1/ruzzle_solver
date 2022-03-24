import fileinput
from functools import lru_cache


def read_word_file(file_to_use):
    # old version full file timed at 0.2367s, 0.2450s, 0.2350s
    with open(file_to_use) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


@lru_cache
def read_filtered_word_file(file_to_use, valid_letters):
    # filtered version full file timed at 0.3859s, 0.4114s
    iterator = fileinput.input(file_to_use)
    return {line.strip() for line in iterator if line[0] in valid_letters}
