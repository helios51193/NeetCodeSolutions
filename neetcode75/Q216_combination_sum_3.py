from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtracking(start, path, target, k):
            if target == 0 and k == 0:
                res.append(path[:])
                return
            
            for i in range(start,10):
                if i > target or k <=0:
                    break
                
                path.append(i)
                backtracking(i+1, path, target -i, k-1)
                path.pop()
        
        backtracking(1, [], n, k)
        return res


"""
    Last Looked
    23-02-26

"""  