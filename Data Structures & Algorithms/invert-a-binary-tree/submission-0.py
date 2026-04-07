# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)
    
    