class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        temp = digits[0] * 10

        if len(digits) == 1:
            once = digits[0] + 1
            once = str(once)
            for i in range(len(once)):
                res.append(once[i])
            return res

        for i in range(1, len(digits) - 1):
            temp += digits[i]
            temp = temp * 10
        print("temp before", temp)
        temp += digits[len(digits)-1]
        print("temp after", temp)
        temp += 1
        temp = str(temp)
        for i in range(len(temp)):
            res.append(int(temp[i]))
        return res