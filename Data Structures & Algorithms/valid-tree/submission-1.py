class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        mp = defaultdict(list)

        for src, dst in edges:
            mp[src].append(dst)
            mp[dst].append(src)

        vis= set()
        def dfs(num, parent):
            if num in vis:
                return False
            
            vis.add(num)
            for nei in mp[num]:
                if nei==parent:
                    continue
                if not dfs(nei, num):
                    return False
            
            return True

        

        
        return dfs(0, -1) and len(vis) == n
        # do i have to combine this with connected component checking?
