class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # pair: [temp, index]

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI

            stack.append((n, i))

        return res