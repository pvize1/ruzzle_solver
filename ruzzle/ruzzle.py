"""
TODO: 1) Add environment variable handler
TODO: 2) Run coverage report
"""

from helpers.word_dict import WordDict
from helpers.ruzzle_matrix import RuzzleMatrix

if __name__ == "__main__":
    english_words = WordDict(language="en")
    ruzzle_matrix = RuzzleMatrix(dict_file=english_words.file_to_use)

    print("")
    print(f"Count of words={ruzzle_matrix.word_count}")
    print(f"Matrix={ruzzle_matrix.matrix_string}")

    ruzzle_matrix.navigate_word_dict(ruzzle_matrix.filtered_dict, "", [])
    ruzzle_matrix.draw_matrix()

    for idx in range(len(ruzzle_matrix.words)):
        print(ruzzle_matrix.words[idx], ruzzle_matrix.paths[idx])
