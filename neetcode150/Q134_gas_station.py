
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # if total gas is less than total cose ,return
        if sum(gas) < sum(cost):
            return -1
        
        tank = idx = 0
        # start from 0, if the tank is -ve, reset the tank idx to 0
        # For any value a, if the tank becomes negative. There there is no solution at a or before a a
        # as values before a will just make the tank more negative.
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, idx = 0, i+1

        return idx

"""
    Last Looked
    1-11-25

"""