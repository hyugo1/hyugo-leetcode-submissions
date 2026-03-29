class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        # pairs = pairs[::-1]
        pairs = sorted(pairs, reverse=True)
        for p, s in pairs:
            destination = ((target - p) / s)
            stack.append(destination)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)