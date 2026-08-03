class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[pre].append(crs)
        

        visited = set()
        beingVisited = set()

        def dfs(num):
            if num in beingVisited:
                return False
            
            if num in visited:
                return True

            beingVisited.add(num)

            for nei in adj[num]:
                if not dfs(nei):
                    return False
                    

            beingVisited.remove(num)
            
            visited.add(num)
            res.append(num)

            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res