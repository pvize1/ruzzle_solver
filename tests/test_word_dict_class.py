"""
"""

import pytest
from ruzzle.helpers.word_dict import WordDict
from ruzzle.helpers.decorators import timer


def test_unknown_lang():
    with pytest.raises(KeyError):
        test_words = WordDict(language="de")
        print(test_words)


def test_read_filtered_dict():
    test_words = WordDict(language="test")
    filt_dict = test_words.import_file_to_dict(valid_letters="atatatatatatatat")
    assert filt_dict["a"]["a"]
    assert filt_dict["a"]["a"]["a"]
    assert filt_dict["a"]["t"]


@timer
def test_filter_word_dict():
    test_words = WordDict(language="en")
    filt_dict = test_words.import_file_to_dict(valid_letters="abcdefghijklmnot")
    assert filt_dict["t"]["a"]["b"]["l"]["e"]
