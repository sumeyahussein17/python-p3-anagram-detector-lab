# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, word_list):
        return [
            w for w in word_list
            if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word
        ]
