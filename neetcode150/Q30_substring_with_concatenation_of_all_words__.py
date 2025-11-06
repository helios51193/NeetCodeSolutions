from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        
        if not s or not words:
            return []
        
        word_len = (len(words[0]))
        num_words = len(words)
        total_len = word_len * num_words

        if len(s) < total_len:
            return []
        
        target = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            cur_count = Counter()
            words_used = 0

            for right in range(offset, len(s) - word_len + 1, word_len):

                w = s[right:right+word_len]

                if w in target:
                    cur_count[w] += 1
                    words_used += 1
                
                    while cur_count[w] > target[w]:
                        left_word = s[left:left + word_len]
                        cur_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                     # If we have exactly num_words, record left
                    if words_used == num_words:
                        res.append(left)

                        # move left forward by one word to continue searching
                        left_word = s[left:left + word_len]
                        cur_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                else:
                    # reset the window if word not in target
                    cur_count.clear()
                    words_used = 0
                    left = right + word_len
        
        return sorted(res)

"""
    Last Looked
    6-11-25

"""




        