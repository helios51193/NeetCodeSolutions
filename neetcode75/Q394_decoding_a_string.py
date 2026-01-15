class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        num = 0

        for char in s:
            print(char)
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((current_string, num))
                current_string = ""
                num = 0
            elif char == "]":
                last_string, repeat_count = stack.pop()
                current_string = last_string + current_string * repeat_count
            else:
                current_string += char
            
            print(f"{char=}, {stack=}, {current_string=}")
        return current_string

"""
    Last Looked
    15-01-26

""" 