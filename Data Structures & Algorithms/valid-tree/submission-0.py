class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for src, dst in edges:
            mp[src].append(dst)

            
        visited = set()
        beingvisited = set()
        def dfs(num):
            if num in beingvisited:
                return False
            if num in visited:
                return True
            beingvisited.add(num)
            for nei in mp[num]:  
                dfs(nei)            
            beingvisited.remove(num)
            visited.add(num)
            return True
        count =0
        for i in range(n):
            if dfs(i):
                count+=1
            elif len(mp[i]) == 0 or count>1 or not dfs(i):
                return False


        return True
        # do i have to combine this with connected component checking?