class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        oneset = set()
        for n in nums:
            if n in oneset:
                return True
            
            oneset.add(n)
        
        return False