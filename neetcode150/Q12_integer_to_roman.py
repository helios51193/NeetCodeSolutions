# Solution 1
class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1000: "M", 900: "CM",
            500: "D",  400: "CD",
            100: "C",  90: "XC",
            50: "L",   40: "XL",
            10: "X",   9: "IX",
            5: "V",    4: "IV",
            1: "I", 
        }
        r = ""

        for key,value in num_map.items():
            while key <=num:
                r+= value
                num -=key
        
        return r


        