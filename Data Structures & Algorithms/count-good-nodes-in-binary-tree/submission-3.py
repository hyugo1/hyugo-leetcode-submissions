# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None

        stack = [(root, root.val)]
        res = 0

        while stack:
            node, val = stack.pop()
            if val <= node.val:
                res += 1
                
            new_val = max(val, node.val)

            if node.left:
                stack.append((node.left, new_val))
            if node.right:
                stack.append((node.right, new_val))

        return res
                