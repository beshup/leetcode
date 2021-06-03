# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height) - 1 
        maxArea = 0
        while (a < b):
            area = min(height[a], height[b]) * (b - a)
            maxArea = max(area, maxArea)
            if height[a] <= height[b]:
                a += 1
            else:
                b -= 1

        return maxArea
