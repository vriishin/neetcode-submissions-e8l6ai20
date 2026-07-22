class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build a graph, check if there are cycles?
        # topsort is dfs with the extra step of adding a node once youve visited all its children
        # topsort + check cycle in the resulting course array? or if a number appears more than once?
        # how to build topological sort--> dfs, hit all neighbors, once youo have then add that node to a liset. if you can't go back up anymore,
        # then pick the next node on the adj list
        # how ot build an adj list --> iterate through prereqs and then key is first numer in array and then add second num to values for that key
        # how to make values an array in map?
        #pre = defaultdict(list) or

        top = []
        pre = {}
        visited = set()
        for course in range(numCourses):
            pre[course] = []


        for course, prereq in prerequisites:
            pre[course].append(prereq)

        visited = set()   
        path = set()     

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for prereq in pre[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True