class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # true topsort 
        prereq = defaultdict(list)
        for src, dst in prerequisites:
            prereq[src].append(dst)
        # another way to do it is {i: [] for }

        
        visited, cycle = set(), set()
        top = []
       

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for nei in prereq[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            top.append(node)
            visited.add(node)
            return True
            
        for num in range(numCourses):
            if not dfs(num):
                return []

        
        return top











