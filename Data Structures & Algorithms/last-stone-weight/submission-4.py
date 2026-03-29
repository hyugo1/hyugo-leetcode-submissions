class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)> 1:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            cur = a - b

            if cur:
                stones.append(cur)

        return stones[0] if stones else 0