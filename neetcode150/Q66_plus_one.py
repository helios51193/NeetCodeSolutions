
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        for i in range(len(digits)-1,-1, -1):
            if digits[i] == 9:
                digits[i] = 0
            
            else:
                digits[i] = digits[i] + 1
                return digits
            
        # case when all are 9s -> it didnt go to the else
        return [1] + digits


"""
    Last Looked
    07-12-25

"""   