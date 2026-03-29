class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        nums.sort()

        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                length = 0
                current = nums[i]
                while current in numset:
                    length += 1
                    current += 1
                
                longest = max(longest, length)
            


        return longest