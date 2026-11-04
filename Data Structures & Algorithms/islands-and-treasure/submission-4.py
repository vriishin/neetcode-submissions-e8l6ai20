class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647

        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c, 0))
        
        while q:
            for _ in range(len(q)):

                r, c, level = q.popleft()
                neighbors  = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]

                for nr, nc in neighbors:
                    
                    if min(nr,nc)<0 or nr == ROWS or nc ==COLS or grid[nr][nc]!=inf:
                        continue 
                    grid[nr][nc]=level+1
                    q.append((nr,nc,level+1))
                    
            

                    # [2147483647,   -1   ,        0,        2147483647],
                    # [2147483647,2147483647, 2147483647,      -1],
                    # [2147483647,    -1,     2147483647,      -1],
                    # [     0,        -1     ,2147483647,    2147483647]

                    # [1,-1,0,2],
                    # [6,1,2,-1],
                    # [3,-1,3,-1],
                    # [0,-1,5,4]