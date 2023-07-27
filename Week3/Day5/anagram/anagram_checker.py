class AnagramChecker:
    def __init__(self, file) -> None:
        with open(file, "r")  as word_file :
            all_text = word_file.read()
        self.word_list = all_text.split()

    def is_valid_word(self, word: str):
        if word.upper() in self.word_list:
            return True
        else:
            return False
    def get_anagrams(self, word: str):
        result_list = []
        for x in self.word_list:
            if len(x) == len(word):
                if (x == word.upper()):
                    continue
                the_word = sorted(x)
                input_word = sorted(word.upper())
                if (the_word == input_word):
                    result_list.append(x)
        return result_list
