class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res = []

        def backtracking(index, comb, total):
            if total == target:
                res.append(comb[:])
                return
            

            if total > target or index >= len(candidates):
                return
            
            comb.append(candidates[index])
            backtracking(index, comb, total + candidates[index])
            comb.pop()
            backtracking(index+1, comb, total)
        
            return res
        
        return backtracking(0, [], 0)


"""
    Last Looked
    28-11-25

""" 