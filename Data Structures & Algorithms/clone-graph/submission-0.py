"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if not root:
            return None

        q = deque()
        q.append(root)
        # hashmap to relate nodes from original graph to their copies which i will create. 
        # create copies of each node while iterating through the neighbors of athe original node
        mp = {}
        mp[root] = Node(root.val)

        
        while q:
            node = q.popleft()
            #does this create a second copy of root?
            for nei in node.neighbors:
                
                if nei not in mp:
                    q.append(nei)
                    mp[nei] = Node(nei.val)
                mp[node].neighbors.append(mp[nei])
            


        return mp[root]

        

        