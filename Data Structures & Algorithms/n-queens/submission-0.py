class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = []
        for r in range(n):
            row = []
            for c in range(n):
                row.append('.')
            board.append(row)

        def validQ(board, r, c): #curboard, cur row, cur col
            #no other Q in same row, col, diagonal.
            count = 0 
            for row in range(len(board)):
                if row == r:
                    continue
                if board[row][c] == 'Q':
                    count+=1
            for col in range(len(board[0])):
                if col == c:
                    continue
                if board[r][col] == 'Q':
                    count +=1
            
           
            # diagonal check
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if row == r and col == c:
                        continue

                    if abs(row - r) == abs(col - c) and board[row][col] == 'Q':
                        count += 1


            if count>0:
                return False
            else:
                return True
        
        def backtrack(ROW):
            if ROW>=n:
                outputboard = [''.join(row) for row in board]
                res.append(outputboard)
                return
            
            #choices are put Q in this COL or don't 
            for col in range(len(board[ROW])):
                if not validQ(board, ROW, col):
                    continue
                board[ROW][col] = 'Q'
                backtrack(ROW+1)
                board[ROW][col] = '.'

        backtrack(0) 
        return res


            
