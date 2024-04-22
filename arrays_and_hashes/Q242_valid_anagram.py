#Solution 1 - using dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anag = {}
        # count the alphabets in the source string
        for i in s:
            if i not in anag:
                anag[i] = 1
            else:
                anag[i] +=1
        
        # decrement the occurence from the target string
        for j in t:
            if j not in anag.keys():
                return False
            else:
                anag[j] -=1
        # check if all are zero
        all_true = [ x == 0 for x in anag.values()]
        return all(all_true)

# Solution 2 - using sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       s_list = list(s)
       t_list = list(t)

       s_list.sort()
       t_list.sort()

       return s_list == t_list

