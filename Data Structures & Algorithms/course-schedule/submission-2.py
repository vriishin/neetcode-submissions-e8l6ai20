class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False  # Cycle: back to a node on this path
            if node in visited:
                return True   # Already checked; safe

            path.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            path.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
