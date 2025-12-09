class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        max_len = max(len(w) for w in wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # try all word lengths up to max_len
            for l in range(1, max_len + 1):
                j = i - l
                if j < 0:
                    break
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]




"""
    Last Looked
    09-12-25

"""