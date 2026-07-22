class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # return board, 
        #
        rows, cols = len(board), len(board[0])
        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == rows - 1 or r == 0 or c == cols - 1 or c == 0):
                    q.append((r,c))

        while q:
            r, c = q.popleft()

            if min(r,c)<0 or r == rows or c==cols or board[r][c]!='O':
                continue

            board[r][c] = 'Safe'

            q.append((r+1,c))
            q.append((r-1,c))
            q.append((r,c+1))
            q.append((r,c-1)) 


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'Safe':
                    board[r][c] = 'O'
 
                