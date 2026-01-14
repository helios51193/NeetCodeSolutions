class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        stack = []

        for ast in asteroids:
            is_alive = True

            while is_alive and stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    is_alive = False
                else:
                    is_alive = False
            
            if is_alive:
                stack.append(ast)
        
        return stack

"""
    Last Looked
    14-01-26

"""  