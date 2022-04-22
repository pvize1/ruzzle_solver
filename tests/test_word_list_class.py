"""
"""

import pytest
from ruzzle.helpers.word_list import WordList
from ruzzle.helpers.decorators import timer


def test_sorted_words():
    test_words = WordList()
    test_words.add_new_word("a", [1], 1)
    test_words.add_new_word("be", [2, 3], 7)
    test_words.add_new_word("ae", [1, 3], 4)
    record_0 = test_words.sorted_words[0]
    record_2 = test_words.sorted_words[2]
    assert record_0.score == 7
    assert record_2.score == 1
