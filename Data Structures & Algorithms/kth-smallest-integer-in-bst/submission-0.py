# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order dfs should return whole tree's values in sorted order.
        arr = []
        self.dfs(root, arr)
        return arr[k-1]

    def dfs(self, root, arr):
        if root is None:
            return
        
        #left, node, right
        self.dfs(root.left,arr)
        arr.append(root.val)
        self.dfs(root.right,arr)
        