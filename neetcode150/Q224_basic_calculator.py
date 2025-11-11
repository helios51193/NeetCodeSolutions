class Solution:
    def calculate(self, s: str) -> int:
        '''
            ans stores the running result
            num stores the currently processing number
            sign stores the current sign of the system (1 is positive -1 is negative)
            If parenthesis are encountered the sign is pushed and then closing is popped when encountered
        '''
        ans = 0
        num = 0
        sign = 1
        stack = [sign]

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "(":
                stack.append(sign)
            elif char == ")":
                stack.pop()
            elif char in ["+","-"]:
                ans += sign * num
                sign = (1 if char == '+' else -1) * stack[-1]
                num = 0
        
        return ans + sign * num

"""
    Last Looked
    11-11-25

"""
