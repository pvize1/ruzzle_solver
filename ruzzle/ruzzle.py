"""
TODO: 1) Add environment variable handler
TODO: 2) Run coverage report
"""

from helpers.ruzzle_matrix import RuzzleMatrix

if __name__ == "__main__":
    multiplier_matrix = [
        ".",
        "2l",
        ".",
        ".",
        ".",
        ".",
        "3w",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        "2w",
        ".",
        ".",
    ]
    ruzzle_matrix = RuzzleMatrix(multipliers=multiplier_matrix, language="en")

    print("")
    print(f"Matrix={ruzzle_matrix.matrix_string}")

    ruzzle_matrix.navigate_word_dict(ruzzle_matrix.filtered_dict, "", [])
    ruzzle_matrix.draw_matrix()
    top_score = ruzzle_matrix.sort_list_words

    for idx in range(10):
        record = top_score[idx]
        print(record.word, record.word_len, record.word_path, record.score)
