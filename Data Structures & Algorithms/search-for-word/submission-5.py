class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        self.res = False

        def dfs(r, c, subset, visited):
            if ''.join(subset) == word or self.res == True:
                self.res = True
                return

            if (
                min(r,c)<0 or r==ROWS or c==COLS or (r,c) in visited or len(subset)>len(word)
                ):
                return
            

            visited.add((r,c))
            
            neighbors = [ 
                [r+1, c], [r-1, c], [r, c+1], [r, c-1]
                           ]
          

            for r2, c2 in neighbors:
                subset.append(board[r][c])
                dfs(r2,c2,subset[:], visited)
                subset.pop()
            
            visited.remove((r,c))
            return self.res
           
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, [], set())
        return self.res
