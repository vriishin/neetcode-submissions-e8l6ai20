# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = 0 

        def dfs(root):
            nonlocal res
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            diff = abs(left - right)

            res = max(res, diff)
            
            return 1 + max(left, right)
        dfs(root)
        if res>1:
            return False
        else: 
            return True
            
            



