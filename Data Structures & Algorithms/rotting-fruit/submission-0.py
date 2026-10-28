class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        healthy =0 
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                if grid[r][c] == 1:
                    healthy+=1
      
        while q: 
            r, c, steps = q.popleft()


            for _ in range(len(q)):
                
                neighbors = [ (r+1, c), (r-1,c), (r, c+1), (r,c-1)]

                for nr, nc in neighbors:
                    if min(nr,nc)<0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue
                    q.append((nr, nc, steps+1))
                    grid[nr][nc] = 2
                    steps+=1

            

   
        
        return steps if healthy>0 else -1
