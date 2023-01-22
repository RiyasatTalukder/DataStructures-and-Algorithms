'''
Given a Sudoku board, the algorithm determines if it is valid through meeting the following conditions:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Time: O(n)
Space: O(n)
'''

def isValidSudoku(board):
    # keep track of visited elements in row x, column y
    rows = [dict() for _ in range(len(board))]
    cols = [dict() for _ in range(len(board[0]))]

    def isValidNum(num):
        return num >= 1 and num <= 9

    def isValidSub(i, j):
        visited = {}
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if board[x][y] == '.':
                    continue
                
                # check if number is valid and meets the conditions
                if (not isValidNum(int(board[x][y])) or board[x][y] in visited 
                or board[x][y] in rows[x] or board[x][y] in cols[y]):
                    return False

                visited[board[x][y]] = ''
                rows[x][board[x][y]] = x
                cols[y][board[x][y]] = y
            
        return True
    
    for i in range(0, len(board), 3):
        for j in range(0, len(board[0]), 3):
            if not isValidSub(i, j):
                return False
    
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

assert isValidSudoku(board) == True