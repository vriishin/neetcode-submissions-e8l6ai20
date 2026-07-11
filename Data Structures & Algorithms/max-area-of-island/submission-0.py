class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if min(r, c)<0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0 :
                return 0
            
            visited.add((r,c))
            neighbors = [ (r+1, c), (r-1, c) , (r, c+1), (r,c-1) ]
            size = 1
            for nr, nc in neighbors:
                size += dfs(nr, nc)
            return size
            
            
        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, dfs(row, col))
                
        return res