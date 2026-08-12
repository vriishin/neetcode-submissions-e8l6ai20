class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # check for existing connection as you add to adjList?
        # INITIALLY ACYCLIC, then edge was added. So search for a cycle and remove one of those edges --> 

        adj = defaultdict(list)

        
        
        def detectCycle(node, parent, visited):
            if node in visited:
                return True
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if detectCycle(nei,node, visited):
                    return True
            return False


        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

            if detectCycle(src, -1, set()):
                return [src,dst]
        return []
