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
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node:
                if node.left and node.left.val>=node.val:
                    return False
                else:
                    q.append(node.left)
                
                if node.right and node.right.val<=node.val:
                    return False
                else:
                    q.append(node.right)
        return True

        