# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    
    #currently disfunctional!
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums) - 1
        res = [-1, -1]

        while (lo <= hi):
            mid = int((hi + lo) / 2)
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid 

            if nums[mid] == target: res[0] = mid
        
        while (lo <= hi):
            mid = lo + int((hi - lo) / 2)
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
            
            if nums[mid] == target: res[1] = mid

        return res

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
        