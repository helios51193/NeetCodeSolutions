class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)
        
        def backtracking(path):
            print(path)
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtracking(path)
                path.pop()

        
        res = []
        backtracking([])
        return res


"""
Alternate Solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) <= 1:
            return [nums]
        

        answer = []
        for n in nums:
            rest = [x for x in nums if x != n]
            for p in self.permute(rest):
                answer.append([n] + p)
        
        return answer
        
"""

"""
    Last Looked
    28-11-25

""" 