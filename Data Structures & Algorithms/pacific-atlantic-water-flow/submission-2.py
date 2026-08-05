class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # backtracking O(4^mn)
        # faster way?
        # 
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def dfs(r, c, visited, prev):
            if (r,c) in visited or min(r,c)<0 or r == ROWS or c == COLS or heights[r][c]<prev:  
                #checking if heights[r][c] LESS THAN prevHeight because this method doesn't exactly do the natural idea of checking if an individual cell can reach both, rather inverts it to see how far the border cells can reach in the opposite direction. It adds those cells to the ocean the border is touching. 
                return
            visited.add((r,c))
            neighbors = [   (r+1, c),
                            (r-1, c),
                            (r, c+1),
                            (r, c-1)    ]
            
            for nr,nc in neighbors:
                dfs(nr, nc, visited, heights[r][c])

        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) #these cells touch the pacific, and reach out to see if what they touch is in the pacific.
            dfs(r, COLS-1, atl, heights[r][COLS-1]) #these cells touch the atlantic, and reach out to see if what they touch is in the atlantic

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #same as first in Rows dfs]
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # same as second in cols dfs


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c]) 
        
        return res