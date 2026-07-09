class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0 
        def dfs(row, col):
            if (row, col) in visited or min(row, col)<0 or row==ROWS or col == COLS or grid[row][col] == "0":
                return
            
            visited.add((row,col))


            neighbors = [ (row+1, col), (row-1, col), (row, col+1), (row, col-1)]

            for nr, nc in neighbors:
                dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    res+=1
        return res
                