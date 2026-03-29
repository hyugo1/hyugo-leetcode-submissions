class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #temp, index

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                indexT, indexI = stack.pop()
                res[indexI] = i - indexI

            stack.append((t, i))

        return res