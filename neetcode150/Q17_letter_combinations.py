class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        if not digits:
            return []
        
        phone_map = {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi", 
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtracking(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtracking(index+1, path)
                path.pop() #backtrack
        
        
        combinations = []
        backtracking(0,[])
        return combinations

"""
    Last Looked
    28-11-25

""" 