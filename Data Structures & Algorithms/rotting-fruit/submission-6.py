class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                

        while q: 
            qlen = len(q)

            for _ in range(qlen):
                r, c = q.popleft()
                neighbors = [(r,c+1), (r,c-1), (r+1, c), (r-1,c)]
                
                for nr, nc in neighbors:
                    if min(nr,nc)<0 or nr ==ROWS or nc == COLS or grid[nr][nc]==2 or grid[nr][nc]==0:
                        continue
                    
                    grid[nr][nc] = 2
                
                    q.append((nr,nc))
            res+=1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        print(grid)
        return max(0,res-1)
        