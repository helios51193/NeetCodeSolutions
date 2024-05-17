#without stack
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        count = 0
        # calculate the time required to reach target for each fleet (each single car can also be a fleet)
        time_taken = {position[i]:(target-position[i])/speed[i] for i in range(len(position))}
        
        sorted_time_taken = sorted(time_taken.items(), key=lambda x:x[0], reverse=True)

        max_time = 0
        for x,y in sorted_time_taken:
            if y > max_time:
                count +=1
                max_time = y
        return count

#with stack
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        memo = sorted(zip(position,speed), key=lambda x:x[0], reverse=True)
        stack = []
        for p,s in memo:
            if stack:
                rd = (target - stack[-1][0])/stack[-1][1]
                ld = (target - p)/s
                if ld > rd:
                    stack.append((p,s))
            else:
                stack.append((p,s))
        
        return len(stack)
