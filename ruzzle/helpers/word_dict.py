"""
xTODO: 1) Change debug to language ("en" or "test"), rename text files
xTODO: 2) Save english dictionary to file - CANCELLED
TODO: 3) Remove path from dict_files, and use curr/tree to search for file, check for existence
TODO: 4) Raise error if language/file not found
"""


dict_files = {
    "en": "words_english.txt",
    "test": "words_test.txt",
}
base_path = "../wordfiles/"


class WordDict:
    def __init__(self, language="test"):
        language = language.lower()
        try:
            self._file_to_use = base_path + dict_files[language]
        except KeyError:
            raise KeyError(f"Language {language} not available")
        self._language = language

    @property
    def language(self):
        return self._language

    @property
    def file_to_use(self):
        return self._file_to_use
