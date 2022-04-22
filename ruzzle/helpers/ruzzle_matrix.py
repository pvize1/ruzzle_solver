"""
TODO: 1) Combine Words and Path to data structure (dict?)
2) in code
TODO: 3) Add letter scores and multipliers to matrix
TODO: 4) Select best path based on score, sort descending
TODO: 5) Remove word_count (alter tests?)
TODO: 6) Use Numpy
TODO: 7) Create Path Class
"""

from random import choice
from .word_dict import WordDict
from .word_list import WordList

_next_cell = [
    [1, 4, 5],
    [0, 2, 4, 5, 6],
    [1, 3, 5, 6, 7],
    [2, 6, 7],
    [0, 1, 5, 8, 9],
    [0, 1, 2, 4, 6, 8, 9, 10],
    [1, 2, 3, 5, 7, 9, 10, 11],
    [2, 3, 6, 10, 11],
    [4, 5, 9, 12, 13],
    [4, 5, 6, 8, 10, 12, 13, 14],
    [5, 6, 7, 9, 11, 13, 14, 15],
    [6, 7, 10, 14, 15],
    [8, 9, 13],
    [8, 9, 10, 12, 14],
    [9, 10, 11, 13, 15],
    [10, 11, 14],
]
_letter_scores = {
    "a": 1,
    "e": 1,
    "i": 1,
    "o": 1,
    "u": 1,
    "l": 1,
    "n": 1,
    "r": 1,
    "s": 1,
    "t": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10,
}
_letter_distribution = "aabcdeeeefghiiijklmnoopqrrrssstttuuvwxyz"
_end = "_end_"


class RuzzleMatrix:
    def __init__(self, input_string="", multipliers="", language="test"):
        if len(input_string) == 16 and input_string.isalpha():
            self._matrix_string = input_string.lower()
        else:
            self._matrix_string = self._create_matrix()
        if len(multipliers) == 16:
            self._multipliers = multipliers
        else:
            self._multipliers = ["."] * 16
        self._words = WordList()
        word_dict = WordDict(language)
        self._filtered_dict = word_dict.import_file_to_dict(set(self._matrix_string))

    def navigate_word_dict(self, next_dict_level, word, paths):
        prev_word = word
        prev_paths = paths
        success = False

        for letter in next_dict_level.keys():
            if letter == _end:
                score, path = self._get_best_path(word, paths, self._multipliers)
                self._words.add_new_word(word, path, score)
            else:
                word = prev_word + letter
                paths = self._check_path_to_letter(letter, prev_paths)
                if paths:
                    success = self.navigate_word_dict(
                        next_dict_level[letter], word, paths
                    )
        return success

    def _check_path_to_letter(self, letter, paths):
        new_paths = []
        if not paths:
            matrx_idx = 0
            for matrix in self._matrix_string:
                if matrix == letter:
                    new_paths.append([matrx_idx])
                matrx_idx += 1
        else:
            for path in paths:
                for cell in _next_cell[path[-1]]:
                    if self._matrix_string[cell] == letter and cell not in path:
                        new_paths.append([*path, cell])
        return new_paths

    def draw_matrix(self):
        print("")
        print("-+-+-+-")
        for x in range(4):
            for y in range(4):
                print(self._matrix_string[x * 4 + y].upper(), end=" ")
            print("")
            print("-+-+-+-")
        print("")

    @staticmethod
    def _create_matrix():
        new_matrix = ""
        for i in range(16):
            new_matrix += choice(_letter_distribution)
        return new_matrix

    @staticmethod
    def _get_best_path(word, paths, multi):
        # TODO: Sort out scoring of paths and pick top score
        base_score = 0
        for letter in word:
            base_score += _letter_scores[letter]

        best_score = 0
        best_path = []
        for path in paths:
            curr_score = base_score
            multiplier = 1
            idx = 0
            for cell in path:
                if multi[cell] != ".":
                    if multi[cell] == "2l":
                        curr_score += _letter_scores[word[idx]]
                    if multi[cell] == "3l":
                        curr_score += (_letter_scores[word[idx]] * 2)
                    if multi[cell] == "2w":
                        multiplier *= 2
                    if multi[cell] == "3w":
                        multiplier *= 3
                idx += 1
            curr_score *= multiplier
            if curr_score > best_score:
                best_score = curr_score
                best_path = path
        return best_score, best_path

    @property
    def matrix_string(self):
        return self._matrix_string

    @property
    def multipliers(self):
        return self._multipliers

    @property
    def sort_list_words(self):
        return self._words.sorted_words

    @property
    def words(self):
        return [word_data.word for word_data in self._words.words]

    @property
    def lengths(self):
        return [word_data.word_len for word_data in self._words.words]

    @property
    def paths(self):
        return [word_data.word_path for word_data in self._words.words]

    @property
    def scores(self):
        return [word_data.score for word_data in self._words.words]

    @property
    def filtered_dict(self):
        return self._filtered_dict
