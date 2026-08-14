class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        res = []
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        for key in adj:
            adj[key].sort(reverse=True)

        def dfs(airport):
            while adj[airport]:
                dst = adj[airport].pop()
                dfs(dst)

            res.append(airport)


        dfs('JFK')
    
        return res[::-1]