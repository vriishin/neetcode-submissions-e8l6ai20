# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bfs(root)

    def bfs(self, root):
        stack = []
        stack.append([root,-float('infinity'),float('infinity')])


        while stack:
            node, left, right = stack.pop()

            if not (left<node.val<right):
                return False
            if node.left:
                stack.append([node.left,left,node.val])
            if node.right:
                stack.append([node.right,node.val,right])
        return True

            #every thing to left of root has upper bound of root.val.
            # similarly, eveyrthing to right has lower bound of root.val, so we pass along root.val to each iter to check.

        