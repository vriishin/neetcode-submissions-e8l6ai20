class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0: 
                    q.append((r,c,0))
        
        while q: 
            qlen = len(q)

            for _ in range(qlen):
                r, c, count  = q.popleft()
                neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                
                if min(r,c)<0 or r==ROWS or c==COLS or grid[r][c] == -1:
                    continue
                
                if grid[r][c]<count:
                    continue
                grid[r][c] = min(count, grid[r][c])

                for nr, nc in neighbors:
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS or grid[nr][nc] == -1 or grid[nr][nc]==0:
                        continue
                    q.append((nr,nc,count+1))
        
        
                
                    