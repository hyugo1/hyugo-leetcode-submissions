class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # index, tmp 


        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                stackI, stackT = stack.pop()
                index = i - stackI
                res[stackI] = index
            
            stack.append((i, n))
        return res