# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return res[k - 1]
 
        def dfs(i, node):
            nonlocal k
            if not node:
                return None
            left = dfs(i, node.left)
            if left is not None:
                return left
            k -= 1
            if k  == 0:
                return node.val
            return dfs(i, node.right)
        return dfs(0, root)