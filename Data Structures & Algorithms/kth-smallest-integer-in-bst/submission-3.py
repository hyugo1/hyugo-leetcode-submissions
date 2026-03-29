# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        # heapq.heapify(heap)
        # min_num = float('inf')
        
        def dfs(node):
            if not node:
                return
            heapq.heappush(heap, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        while k > 0:
            min_num = heapq.heappop(heap)
            k -= 1
        
        return min_num