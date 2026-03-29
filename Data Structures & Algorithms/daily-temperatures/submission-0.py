class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair: [temp, index]
        answer = [0] * len(temperatures)
        # numOfDays = 0

        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                answer[stackIndex] = (i - stackIndex) # numOfDays
            stack.append([temp, i])
        return answer
