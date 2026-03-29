class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens == "":
            return 0

        stack = []
        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b + a)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b - a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(b * a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(float(b) / a)
            else:
                stack.append(int(t))

        print(stack)
        return int(stack[0])