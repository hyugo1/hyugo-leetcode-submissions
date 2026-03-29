class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN > closeN:
                stack.append(")")
                dfs(openN, closeN + 1)
                stack.pop()


            if n > openN:
                stack.append("(")
                dfs(openN + 1, closeN)
                stack.pop()

        
        dfs(0, 0)
        return res