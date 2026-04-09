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
        return self.bfs(root)
    
    def bfs(self, node):
        if root is None:
            return
        q = deque() # queue start
        q.append(root)
        while q: 
            node = q.popleft()
            node.left, node.right = node.right, node.left 
            if node.left: q.append(node.left) 
            if node.right: q.append(node.right)

            #next to iterate through neighbors:
        return root
            
        # how to iterate through whole tree/graph. While queue

        
    
    