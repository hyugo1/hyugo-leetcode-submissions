class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 1
        maxwindownum = 0
        res = []
        temp = []
        tmpmax = float("-inf")
        tempmax = float("-inf")

        for i in range(0, k):
            temp.append(nums[i])
            tempmax = max(temp)
        res.append(tempmax)

        for r in range(k, len(nums)):
            temp.append(nums[r])
            maxwindownum = max(maxwindownum, nums[r])
            while (r - l + 1) > k:
                temp.remove(nums[l])
                l += 1
            
            tmpmax = max(temp)
            res.append(tmpmax)

        return res


            
            



