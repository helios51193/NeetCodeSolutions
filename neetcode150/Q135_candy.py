from typing import List

# One pass solution
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total_candies = n
        i = 1

        while i < n:
            # if both rating are same , increment i and continue
            if ratings[i] == ratings[i-1]:
                i +=1
                continue
            

            # loop till current has high rating than prev, update the peak 
            current_peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                current_peak +=1
                total_candies += current_peak
                i += 1
            
            # return if there are rating in ascending order
            if i == n:
                return total_candies
            
            # loop till current has lower rating than prev, update valley
            current_valley = 0
            while i < n and ratings [i] < ratings[i-1]:
                current_valley +=1
                total_candies += current_valley
                i +=1
            
            # remove the minumum of peak and valley as we add  peack and valley 2 times. 
            total_candies -= min(current_peak, current_valley)
        
        return total_candies

# two pass solution
# also retains the candy distribution
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1,n):
            if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and candies[i+1] >= candies[i]:
                candies[i] = candies[i+1] + 1
        
        total_candies = sum(candies)

        return total_candies

"""
    Last Looked
    1-11-25

"""