import pytest

from ruzzle.helpers.word_dict import WordDict
from ruzzle.helpers.ruzzle_matrix import RuzzleMatrix
from ruzzle.helpers.decorators import timer


@pytest.fixture
def test_word_set():
    return WordDict(language="test")


@timer
def test_navigate_dictionary(test_word_set):
    ruzzle_matrix = RuzzleMatrix(
        "aahdefhhijklmnot", dict_file=test_word_set.file_to_use
    )
    assert ruzzle_matrix.matrix_string == "aahdefhhijklmnot"

    ruzzle_matrix.navigate_word_dict(ruzzle_matrix.filtered_dict, "", [])
    assert len(ruzzle_matrix.words) == 2
    assert len(ruzzle_matrix.paths) == 2
    assert len(ruzzle_matrix.paths[1]) == 2

    print("")
    print(f"Ruzzle matrix:")
    for i in range(4):
        print(ruzzle_matrix.matrix_string[i * 4 : i * 4 + 4])
    print("")

    for idx in range(2):
        print(ruzzle_matrix.words[idx], ruzzle_matrix.paths[idx])


def test_input_string_2chars(test_word_set):
    ruzzle_matrix = RuzzleMatrix("at", dict_file=test_word_set.file_to_use)
    assert len(ruzzle_matrix.matrix_string) != 2


def test_draw_matrix(test_word_set, capsys):
    ruzzle_matrix = RuzzleMatrix(
        "aahdefhhijklmnot", dict_file=test_word_set.file_to_use
    )
    ruzzle_matrix.draw_matrix()
    captured = capsys.readouterr()
    assert (
        captured.out
        == "\n-+-+-+-\nA A H D \n-+-+-+-\nE F H H \n-+-+-+-\nI J K L \n-+-+-+-\nM N O T \n-+-+-+-\n\n"
    )
