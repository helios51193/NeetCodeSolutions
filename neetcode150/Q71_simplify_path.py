class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        for dir in path.split("/"):
            if dir == "" or dir == ".": continue
            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)
