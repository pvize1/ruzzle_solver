"""
"""


class WordData:
    def __init__(self, word, path, score):
        self._word = word
        self._length = len(word)
        self._path = path
        self._score = score

    def __repr__(self):
        return (
            f"WordData({self._word=}, {self._length=}, {self._path=}, {self._score=})"
        )

    def __str__(self):
        return f"{self._word}, {self._length}, {self._path}, {self._score}"

    @property
    def word(self):
        return self._word

    @property
    def word_len(self):
        return self._length

    @property
    def word_path(self):
        return self._path

    @property
    def score(self):
        return self._score


class WordList:
    def __init__(self):
        self._word_list = []

    def add_new_word(self, word, path, score):
        new_word = WordData(word, path, score)
        self._word_list.append(new_word)

    @property
    def words(self):
        return self._word_list

    @property
    def sorted_words(self):
        return sorted(self._word_list, key=lambda d: d.score, reverse=True)
