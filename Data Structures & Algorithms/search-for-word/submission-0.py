class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])


        def dfs(r, c, subset, visited):
            if ''.join(subset) == word:
                return True
    
            neighbors = [ 
                [r+1, c], [r-1, c], [r, c+1], [r, c-1]
                           ]
            
            for r2, c2 in neighbors:
                if min(r2,c2)<0 or r2>=ROWS or c2>=COLS or board[r2][c2] in visited:
                    continue
                visited.add(board[r][c])

                subset.append(board[r][c])
                dfs(r2,c2,subset[:], visited)
                subset.pop() 
                visited.remove(board[r][c])     
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, [], set())
        return False
