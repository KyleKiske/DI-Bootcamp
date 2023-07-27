import string

#Daily Challenge : Text Analysis

class Text:
    def __init__(self, text: str) -> None:
        self.text = text
    def freq_of_word(self, word):
        return(self.text.split().count(word))
    def most_common(self):
        word_count = {}
        most_common_word = ""
        most_common_count = -1
        word_list = self.text.split(" ")
        for word in word_list:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
        for key,value in word_count.items():
            if value > most_common_count:
                most_common_count = value
                most_common_word = key
        return most_common_word
    def unique_words(self):
        word_list = self.text.split(" ")
        word_set = set(word_list)
        return(list(word_set))
    @classmethod
    def from_file(self, filename):
        with open(filename, "r")  as text_file :
            all_text = text_file.read() #read the file
        return Text(all_text)
    
example = Text("aaaaa s d f f f d d d")
print(example.most_common())
print(example.freq_of_word("f"))    
print(example.unique_words())

text_from_file = Text.from_file("the_stranger.txt")
print(text_from_file.most_common())
print(text_from_file.freq_of_word('the'))
print(len(text_from_file.unique_words()))

class TextModification(Text):
    def zero_punctuation(self):
        new_text = self.text.translate((str.maketrans('', '', string.punctuation)))
        return new_text
    def zero_stopwords(self):
        new_text = ""
        with open("stopwords.txt", "r")  as text_file :
            stopwords = text_file.read() #read the file
        word_list = self.text.split()
        stop_set = set(stopwords.split(" "))
        for w in word_list:
            if w.lower() not in stop_set:
                new_text += (" " + w)
        return(new_text)
    
example2 = TextModification(text_from_file.text)

print(f"The lenght of text is {len(example2.text)}")
print(f"The lenght of text without punctuation is {len(example2.zero_punctuation())}")
print(f"The lenght of text without stop words is {len(example2.zero_stopwords())}")
