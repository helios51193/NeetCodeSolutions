from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.words = defaultdict(list)
        
    # size of word : list of words
    def addWord(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        n = len(word)

        # special case , we need to check if all the word characters either in the iteration word or is "."
        if '.' in word:
            for w in self.words[n]:
                if all(word[i] in (w[i], '.') for i in range(n)):
                    return True
            else:
                return False
        
        # directly check if the word exist
        return word in self.words[n]


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


"""
Alternate solution
class WordDictionary:
    def __init__(self):
        self.dictionary = defaultdict(set)
        self.searched = dict()
        
    def addWord(self, word: str) -> None:
        self.dictionary[len(word)].add(word)
        
    def search(self, word: str) -> bool:
        n = len(word)
        key = (word, len(self.dictionary[n]))

        if key in self.searched:
            return self.searched[key]
        
        for w in self.dictionary[n]:
            i = 0

            while i < n and (w[i] == word[i] or word[i] == '.'):
                i += 1

            if i == n:
                self.searched[key] = True

                return True
        self.searched[key] = False
        return False

"""

"""
    Last Looked
    27-11-25

""" 