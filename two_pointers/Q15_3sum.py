'''
    example 1,2,3,4,5,6,7
    we try to find the combinations first between 
    1 and 2,3,4,5,6,7
    next 2 and 3,4,5,6,7
    next 3 and 4,5,6,7
    and so on.
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_n = sorted(nums)
        print(f'sorted: { sorted_n}')
        triplets = []
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        for i in range(len(sorted_n)-2):
            if i > 0 and sorted_n[i] == sorted_n[i-1]:
                continue #number in a triplet should not be same

            left = i+1
            right = len(sorted_n) -1

            while left < right:
                three_sum = sorted_n[i] + sorted_n[left] + sorted_n[right]
                if three_sum == 0 :
                    triplets.append([sorted_n[i], sorted_n[left], sorted_n[right]])
                    left += 1
                    right -= 1
                
                    while sorted_n[left] == sorted_n[left-1] and left < right:
                        left += 1

                    while sorted_n[right] == sorted_n[right+1] and left < right:
                        right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
            
        return triplets


        