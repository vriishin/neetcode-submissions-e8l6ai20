class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        visited, path = set(),set()
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[pre].append(crs)
        
   
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            #backtracking pattern 
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            path.remove(node)

            visited.add(node)

            res.append(node)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
  
        return res