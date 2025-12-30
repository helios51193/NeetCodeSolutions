class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        

        # There are 3 number left, middle, right
        # "first"= left, "middle"=right
        # The loop will go on reassigning first and second till we get a n which is smaller than both 
        # If we get any number greater greater than first or second , the cycle will continue.
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <=first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        
        return False

"""
    Last Looked
    30-12-25

"""  