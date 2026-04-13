# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = self.dfs(root, root.val)
        return count
    
    def dfs(self, root, maxNum):
        if root is None:
            return 0
        
        if root.val>=maxNum:
            maxNum = max(root.val, maxNum)
            return 1 + self.dfs(root.left, maxNum) + self.dfs(root.right, maxNum)
        
        return 0 + self.dfs(root.left, maxNum) + self.dfs(root.right, maxNum)
        