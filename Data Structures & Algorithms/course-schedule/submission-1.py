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
        adjList = {}
        top = []
        for course in range(numCourses):
            adjList[course] = []

        for src, dst in prerequisites:
            adjList[dst].append(src)
        visited = set()
        beingVisited = set()
        def dfs(num):
            if num in beingVisited:
                return False
            if num in visited:
                return True

            beingVisited.add(num)

            for nei in adjList[num]:
                if not dfs(nei):
                    return False

            beingVisited.remove(num)
            visited.add(num)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False



        return True


        