class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if "+" == tokens[i]:
                stack.append((stack.pop()) + (stack.pop()))

            elif "-" == tokens[i]:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            
            elif "*" == tokens[i]:
                stack.append((stack.pop()) * (stack.pop()))
            
            elif "/" == tokens[i]:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(tokens[i]))


        return stack[0]
