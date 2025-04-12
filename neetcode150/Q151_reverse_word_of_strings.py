# The pythonic way
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

# The non pythonic way
class Solution:
    def reverseWords(self, s: str) -> str:
        res  = []
        temp = ""
        for c in s: # loop through the string and extract word in temp
            if c != " ":
                temp += c
            elif temp != "":
                res.insert(0,temp) # insert the work in fromt every time , stack can also be used
                temp = ""
        
        if temp != "":
            res.insert(0, temp)

        return " ".join(res)