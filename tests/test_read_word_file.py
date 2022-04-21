"""
xTODO: 1)
"""

import pytest

from ruzzle.helpers.word_dict import WordDict
from ruzzle.helpers.ruzzle_matrix import RuzzleMatrix
from ruzzle.helpers.decorators import timer


def test_test_file_read():
    test_words = WordDict(language="test")
    assert test_words.file_to_use == "../wordfiles/words_test.txt"


def test_unknown_lang():
    with pytest.raises(KeyError):
        test_words = WordDict(language="de")


def test_eng_file_read():
    test_words = WordDict(language="en")
    assert test_words.file_to_use == "../wordfiles/words_english.txt"


@timer
def test_test_word_file_length():
    ruzzle = RuzzleMatrix("atatatatatatatat", "test")
    assert ruzzle.word_count == 3
    assert ruzzle.filtered_dict["a"]["t"]


@timer
def test_filter_word_file_length():
    ruzzle = RuzzleMatrix("abcdefghijklmnot", "en")
    assert ruzzle.word_count == 26003
    assert ruzzle.filtered_dict["t"]["a"]["b"]["l"]["e"]
