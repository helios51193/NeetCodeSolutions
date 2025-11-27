from collections import deque
from typing import List

# check Q909
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        word_queue = deque()
        word_queue.append(beginWord)

        distance = 1

        while word_queue:
            level_size = len(word_queue)
            for _ in range(level_size):
                
                current_word = word_queue.popleft()
                if current_word == endWord:
                    return distance
                
                for i in range(len(current_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == current_word[i]:
                            continue 
                        
                        new_word = current_word[:i] + c + current_word[i+1:]
                        if new_word in wordSet:
                            word_queue.append(new_word)
                            wordSet.remove(new_word)
            distance += 1
        
        return 0

"""
    Alternate solution
    Instead of checking all 26 letters.do the following 2 things
    Calculate the distance between the current work and words from the set and visit (add to queue) the one with distance 1
    Mantain a set of visited and only visit the ones which are not in the set
"""

"""
    Last Looked
    20-11-25

""" 