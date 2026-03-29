class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {')' : '(', '}' : '{', ']': '['}


        for i in s:
            if i in par:
                if stack and stack[-1] == par[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)

        return True if not stack else False
                