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
                 
