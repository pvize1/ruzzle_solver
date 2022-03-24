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
import fileinput

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
    "a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10,
}
_letter_distribution = "aabcdeeeefghiiijklmnoopqrrrssstttuuvwxyz"
_end = "_end_"

class RuzzleMatrix:
    def __init__(self, input_string="", dict_file=""):
        if len(input_string) != 16:
            self._matrix_string = self._create_matrix()
        else:
            self._matrix_string = input_string.lower()
        self.valid_letters = set(self._matrix_string)
        self._file_to_use = dict_file
        self._words = list()
        self._word_count = 0
        self._paths = list()
        self._level = 0
        self._filtered_dict = self._import_file_to_dict()

    def _import_file_to_dict(self):
        iterator = fileinput.input(self._file_to_use)

        root = dict()

        for line in iterator:
            word = line.split()[0]
            if self._are_letters_valid(word, self.valid_letters):
                self._word_count += 1
                current_value = root
                for letter in word:
                    current_value = current_value.setdefault(letter, {})
                current_value.setdefault(_end, _end)
        return root

    def navigate_word_dict(self, next_dict_level, word, paths):
        prev_word = word
        prev_paths = paths
        self._level += 1
        success = False

        for letter in next_dict_level.keys():
            if letter == _end:
                self._words.append(word)
                score, path = self._get_best_path(paths)
                self._paths.append(path)
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
            # xTODO: 2) Remove path_idx
            # path_idx = 0
            for path in paths:
                for cell in _next_cell[path[-1]]:
                    if self._matrix_string[cell] == letter and cell not in path:
                        new_paths.append([*path, cell])
                        # new_paths.append([])
                        # new_paths[path_idx] = [*path, cell]
                        # path_idx += 1
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
    def _are_letters_valid(word, valid_letters):
        if len(word)<2:
            return False
        for letter in word:
            if letter not in valid_letters:
                return False
        return True

    @staticmethod
    def _get_best_path(paths):
        return 0, paths[0]

    @property
    def matrix_string(self):
        return self._matrix_string

    @property
    def words(self):
        return self._words

    @property
    def paths(self):
        return self._paths

    @property
    def word_count(self):
        return self._word_count

    @property
    def filtered_dict(self):
        return self._filtered_dict
