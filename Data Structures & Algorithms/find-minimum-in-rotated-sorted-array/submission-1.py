from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            # Compare middle element with rightmost element
            if nums[m] > nums[r]:
                # Minimum must be in the right part
                l = m + 1
            else:
                # Minimum is in the left part including middle
                r = m
        
        # After the loop, l == r and points to the smallest element
        return nums[l]