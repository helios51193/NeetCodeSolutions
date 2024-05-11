class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                current = stack.pop()
                result[current] = index - current
            stack.append(index)
        return result