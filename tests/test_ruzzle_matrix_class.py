from ruzzle.helpers.ruzzle_matrix import RuzzleMatrix
from ruzzle.helpers.decorators import timer


def test_input_matrix_set():
    ruzzle_matrix = RuzzleMatrix(input_string="atatatatatatatat", language="test")
    assert ruzzle_matrix.matrix_string == "atatatatatatatat"


def test_input_string_2chars():
    ruzzle_matrix = RuzzleMatrix("at", "test")
    assert len(ruzzle_matrix.matrix_string) != 2


def test_input_string_not_char():
    ruzzle_matrix = RuzzleMatrix("a...............", "test")
    assert len(ruzzle_matrix.matrix_string) != "a..............."


def test_multiplier_set():
    multi = ["-"] * 16
    ruzzle_matrix = RuzzleMatrix(input_string="atatatatatatatat", multipliers=multi, language="test")
    assert ruzzle_matrix.multipliers == multi


def test_multiplier_2chars():
    ruzzle_matrix = RuzzleMatrix(input_string="..", multipliers=["", ""], language="test")
    assert len(ruzzle_matrix.multipliers) != 2


@timer
def test_navigate_dictionary():
    ruzzle_matrix = RuzzleMatrix("aahdefhhijklmnot", "test")
    ruzzle_matrix.navigate_word_dict(ruzzle_matrix.filtered_dict, "", [])
    assert len(ruzzle_matrix.words) == 2
    assert len(ruzzle_matrix.paths) == 2
    assert len(ruzzle_matrix.paths[1]) == 3
    assert ruzzle_matrix.scores[1] == 6
    assert ruzzle_matrix.lengths[1] == 3

    print("")
    print(f"Ruzzle matrix:")
    for i in range(4):
        print(ruzzle_matrix.matrix_string[i * 4: i * 4 + 4])
    print("")

    for idx in range(2):
        print(ruzzle_matrix.words[idx], ruzzle_matrix.paths[idx])


def test_draw_matrix(capsys):
    ruzzle_matrix = RuzzleMatrix("aahdefhhijklmnot", "test")
    ruzzle_matrix.draw_matrix()
    captured = capsys.readouterr()
    assert (
            captured.out
            == "\n-+-+-+-\nA A H D \n-+-+-+-\nE F H H \n-+-+-+-\nI J K L \n-+-+-+-\nM N O T \n-+-+-+-\n\n"
    )
