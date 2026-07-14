class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() #[ starting position, running distance]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,0))

        while q:
            startr, startc, rd = q.popleft()

            neighbors = [(startr+1,startc), (startr-1,startc), (startr,startc+1), (startr,startc-1)]
            for r, c in neighbors:
                if min(r,c)<0 or r == ROWS or c== COLS:
                    continue

                if grid[r][c] == INF:
                    grid[r][c] = rd+1
                    q.append((r,c,rd+1))
                else: 
                    continue

        

        return None
        




        
        