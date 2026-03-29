class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        

        for i in s:
            if i not in hashmap:
                stack.append(i)
                continue

            elif not stack or stack[-1] != hashmap[i]:
                return False

            stack.pop()
        return not stack

            



            