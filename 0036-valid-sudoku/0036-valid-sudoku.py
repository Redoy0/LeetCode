class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #to validate rows
        for i in range(9):
            my_set=set()
            for j in range(9):
                if board[i][j] in my_set:
                    return False
                elif board[i][j] != '.':
                    my_set.add(board[i][j])
        #to validate collumns
        for i in range(9):
            my_set=set()
            for j in range(9):
                if board[j][i] in my_set:
                    return False
                elif board[j][i] != '.':
                    my_set.add(board[j][i])
        #to validate grid
        grid=[(0,0),(0,3),(0,6),
              (3,0),(3,3),(3,6),
              (6,0),(6,3),(6,6)]
        for i,j in grid:
            my_set=set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    if board[r][c] in my_set:
                        return False
                    elif board[r][c] != '.':
                        my_set.add(board[r][c])
        return True