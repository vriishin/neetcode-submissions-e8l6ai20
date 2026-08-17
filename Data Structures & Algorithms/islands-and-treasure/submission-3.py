class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j,0))
        inf = 2147483647
        while q: 
            for _ in range(len(q)):
                r, c, level = q.popleft()
           

                nei = [ (r+1, c), (r-1, c), (r, c+1), (r,c-1) ]
                for nr, nc in nei:
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS or grid[nr][nc] != inf:
                        continue
                    grid[nr][nc]=level+1
                    q.append((nr,nc,level+1))
        