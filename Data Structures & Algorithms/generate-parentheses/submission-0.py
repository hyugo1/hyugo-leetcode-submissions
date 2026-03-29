class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # hashmap = {"(" : ")"}
        stack = []
        result = []

        # for i in range(n):
        #     if i in hashmap:
        #         stack.append("(")

        #     if i not in n:
        #         stack.append(")")

        def recursiveFunction(front_par, back_par):
            if front_par == back_par == n:
                result.append("".join(stack))
                return 

            if front_par < n:
                stack.append("(")
                recursiveFunction(front_par + 1, back_par)
                stack.pop()
                

            if back_par < front_par:
                stack.append(")")
                recursiveFunction(front_par, back_par + 1)
                stack.pop()



        recursiveFunction(0,0,)
        return result