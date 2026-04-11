# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, x: Optional[TreeNode], y: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()

        if x and y: 
            q1.append(x), q2.append(y)
        elif (x and not y) or (not x and y):
            return False

        while q1 and q2: 
            node1, node2 = q1.popleft(), q2.popleft()
            if node1.val != node2.val:
                return False
            
            if node1.left and node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
            elif node1.left or node2.left:
                return False

            if node1.right and node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
            elif node1.right or node2.right:
                return False
        
        return True
