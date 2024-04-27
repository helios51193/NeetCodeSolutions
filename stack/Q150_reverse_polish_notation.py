class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for c in tokens:
            if c in "+-*/":
                a,b = stack.pop(),stack.pop()
            if c == '+':
                stack.append(b + a)
            elif c == "-":
                stack.append(b - a)
            elif c == '*':
                stack.append(b * a)
            elif c == "/":
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[0]
