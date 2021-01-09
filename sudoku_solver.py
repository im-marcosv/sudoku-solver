from timeit import timeit

board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]
#Print the board with -- and ||
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and not i == 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and not j == 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #Return row and column
    return None

def validate(board, num, pos):
    #Check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and not pos[1] == num:
            return False
    #Check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and not pos[0] == num:
            return False  
    
    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and not (i,j) == pos:
                return False
    return True
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1,10):
        if validate(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = 0
    return False
    
print_board(board)
print()
print(str(timeit('solve(board)', 'from __main__ import solve, board')) + " segundos para resolver el 'Sudoku más dificil del mundo'")

print("\n- - - - - - - - - - - - -\n")

print_board(board)