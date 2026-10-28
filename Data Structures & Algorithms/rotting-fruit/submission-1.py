class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        healthy =0
        mins = 0  
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    healthy+=1

        while q: 
            length = len(q)
            r, c = q.popleft()

            for _ in range(length): #going to a new level iterates count of minutes. If no valid in new level, no mins added
                
                neighbors = [ (r+1, c), 
                               (r-1, c),
                               (r, c+1),
                               (r, c-1) ]

                for nr, nc in neighbors:
                    if min(nr, nc)<0 or nr == rows or nc == cols or grid[nr][nc]!=1:
                        continue
                    
                    q.append((nr, nc))


                    grid[nr][nc] = 2
                    healthy -=1
                mins+=1
                
                
                
        print(mins)
        print(healthy)
        if healthy==0:
            return mins
        else:
            return -1