# Solution-1 - using a map
# when encountering starting bracket, push to stack
# when encountering ending bracket, pop the stack and check if the bracket is the corresponding starting bracket. 
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracketMap = {
            "}":"{",
            ")":"(",
            "]":"[" 
        }

        for c in s:
            if c in bracketMap.values():
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                ch = stack.pop()
                if bracketMap.get(c) != ch:
                    return False
        
        return stack == []      

