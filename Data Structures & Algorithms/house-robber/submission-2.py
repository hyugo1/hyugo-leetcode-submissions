class Solution:
    def rob(self, nums: List[int]) -> int:
        twohousesago = 0
        onehousesago = 0


        for n in nums:
            temp = max(n + twohousesago, onehousesago)
            twohousesago = onehousesago
            onehousesago = temp

        return onehousesago