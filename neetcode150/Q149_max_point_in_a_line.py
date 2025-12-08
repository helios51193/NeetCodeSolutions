from math import inf


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        
        if len(points) <=2:
            return len(points)
        
        def find_slope(p1,p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return inf
            return (y1-y2)*1.0/(x1-x2)
        
        ans = 1
        for i, p1 in enumerate(points):
            slopes = {}
            for j, p2 in enumerate(points[i+1:]):
                slope = find_slope(p1, p2)
                slopes[slope] = slopes.get(slope,1) + 1
                ans = max(slopes[slope], ans)
                
        return ans


"""
    Last Looked
    08-12-25

"""