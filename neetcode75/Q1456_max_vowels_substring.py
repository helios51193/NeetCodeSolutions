class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = "aeiou"
        max_vowels = 0
        curr_vowels = 0
        left=0
        # calculate the first window
        for i in range(k):
            if s[i] in vowels:
                curr_vowels +=1
        
        max_vowels = max(max_vowels, curr_vowels)
        # from k to lengtj
        for i in range(k, len(s)):
            # check the left boundary
            if s[left] in vowels:
                curr_vowels-=1
                left += 1
            else:
                left += 1

            # Check the right boundary
            if s[i] in vowels:
                curr_vowels+=1
            max_vowels=max(max_vowels,curr_vowels)

        return max_vowels

            