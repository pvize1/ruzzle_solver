"""
"""

import fileinput

dict_files = {
    "en": "words_english.txt",
    "test": "words_test.txt",
}
base_path = "../wordfiles/"
_end = "_end_"


class WordDict:
    def __init__(self, language="test"):
        language = language.lower()
        try:
            self._file_to_use = base_path + dict_files[language]
        except KeyError:
            raise KeyError(f"Language {language} not available")

    def import_file_to_dict(self, valid_letters):
        root = dict()

        for line in fileinput.input(self._file_to_use):
            word = line.split()[0]
            if self._are_letters_valid(word, valid_letters):
                current_value = root
                for letter in word:
                    current_value = current_value.setdefault(letter, {})
                current_value.setdefault(_end, _end)
        return root

    @staticmethod
    def _are_letters_valid(word, valid_letters):
        if len(word) < 2:
            return False
        for letter in word:
            # TODO change to for letter in set(word)
            if letter not in valid_letters:
                return False
        return True
