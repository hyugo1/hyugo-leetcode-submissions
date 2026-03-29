# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if not root:
        #     return 0
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res[k - 1]
 
        # res = []
        # def dfs(i, node):
        #     if not node:
        #         return 0
        #     i += 1
        #     if i == k:
        #         return node.val
        #     left = dfs(i, node.left)
        #     if left is not None:
        #         return left
        #     return dfs(i, node.right)
        
        # return dfs(0, root)


