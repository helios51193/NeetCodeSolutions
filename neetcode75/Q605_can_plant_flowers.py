class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        ln = len(flowerbed)
        i = 0
        while i < ln  and n > 0:
            if flowerbed[i] == 1:
                i += 2 # Skip next spot since a flower is planted at i
            elif i == ln -1 or flowerbed[i + 1] == 0:
                n -=1 # planted flower
                i += 2 # Move two steps forward since we just planted
            else:
                i += 3 # Skip to the next possible empty spot
        
        return n <=0


"""
    Last Looked
    21-12-25

"""  