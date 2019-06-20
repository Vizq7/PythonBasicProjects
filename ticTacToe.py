def PrintBoard(row, column, userToken, board):
    if board[row, column] == " ":
        board[row,column] = userToken
    else:
        print("\nCell already has a token!\n")

    for z in range(4):
        for x in range(3):
            print("+", end="")
            for y in range(3):
                print("-", end="")
        print("+", end="\n")
        if z < 3:
            for t in range(3):
                print("|",end=" "+board[z,t]+" ")
            print("|")
    return board

def InitBoard():
    board = {}

    for x in range(4):
        for y in range(3):
            board[x, y] = " "
    
    return board

def CheckBoardStatusH(board, playerToken):
    tokenCount = 0

    for x in range(4):
        if tokenCount != 3:
            for y in range(3):
                if board[x, y] == playerToken:
                    tokenCount += 1
            if tokenCount < 3:
                tokenCount = 0
    
    return tokenCount == 3

def CheckBoardStatusV(board, playerToken):
    tokenCount = 0
    turn = 0

    for x in range(3):
        for y in range(3):
            if tokenCount != 3:
                if board[y, turn] == playerToken:
                    tokenCount += 1
                else:
                    tokenCount = 0
        turn += 1

    return tokenCount == 3

def CheckBoardStatusD(board, playerToken):
    diagonalToken = False

    if board[1, 1] == playerToken:
            diagonalToken = board[2, 2] == playerToken and board[0, 0] == playerToken
            if not diagonalToken:
                diagonalToken = board[0, 2] == playerToken and board[2, 0] == playerToken

    return diagonalToken

def CheckBoardStatus(board, playerToken):
    return CheckBoardStatusH(board, playerToken) or CheckBoardStatusV(board, playerToken) or CheckBoardStatusD(board, playerToken)


userRow = 0
userColumn = 0
userTurn = 0
board = InitBoard()

PrintBoard(0, 0, " ", board)
print("\nWelcome to Tic Tac Toe")

while userRow != "q":
    if userTurn % 2 == 0:
        print("User 1 turn\n")
        userToken = "X"
    else:
        print("User 2 turn\n")
        userToken = "O"

    print("Enter row: ", end = " ")
    userRow = input()
    
    if userRow != "q":
        print("Enter column: ", end=" ")
        userColumn = input()
        try:
            board = PrintBoard(int(userRow)-1, int(userColumn)-1, userToken, board)
            if CheckBoardStatus(board, userToken):
                print("Player wins")
                userRow = "q"
            userTurn +=1
        except:
            pass
    pass

print("Exiting game...")