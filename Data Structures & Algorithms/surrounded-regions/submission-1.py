class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        q = deque()

        for r in range(ROWS): 
            for c in range(COLS):

                if ( r ==0 or r == ROWS-1 or c==0 or  c==COLS-1) and board[r][c] == 'O':
                    q.append((r,c))

        while q: 
            r, c = q.popleft()
            
            neighbors= [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]
            if board[r][c]=='O':    
                board[r][c] ='T'
                for nr, nc in neighbors: 
                    if min(nr,nc)<0 or nr==ROWS or nc==COLS:
                        continue
                    q.append((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c]='X'
                if board[r][c] == 'T':
                    board[r][c] ='O'

        