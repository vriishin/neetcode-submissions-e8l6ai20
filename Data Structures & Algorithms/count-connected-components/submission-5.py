class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        res = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for nei in adj[node]:
                dfs(nei)
            
            
            return 

        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res+=1
        
        return res
            
