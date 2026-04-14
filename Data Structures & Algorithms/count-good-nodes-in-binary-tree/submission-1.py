# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, node, maxNum):
        if node is None:
            return 0 

        if node.val>=maxNum: 
            return 1 + self.dfs(node.left,max(node.val,maxNum)) + self.dfs(node.right, max(maxNum,node.val))
        else:
            return 0 + self.dfs(node.left,max(node.val,maxNum)) + self.dfs(node.right, max(maxNum,node.val)) 