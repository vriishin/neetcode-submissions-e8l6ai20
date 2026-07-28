class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        res = 0
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visited =set()
        def dfs(num):
            if num in visited:
                return
            visited.add(num)

            for nei in adj[num]:
                dfs(nei)
            

        for num in range(n):
            if num not in visited: 
                dfs(num)
                res+=1
            
        return res