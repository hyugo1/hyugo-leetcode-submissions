class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(opened, closed):
            if opened == n == closed:
                res.append("".join(stack))
                return
            if opened > closed:
                stack.append(")")
                dfs(opened, closed + 1)
                stack.pop()
            if opened < n:
                stack.append("(")
                dfs(opened + 1, closed)
                stack.pop()

        dfs(0, 0)
        return res