
# ------------- Functions ---------------
# Play a game of tic tac toe
#This function prints the board
def printBoard(board):
    print("\n")
    print(board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9")
    print(board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
    print(board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
    print("\n")
def insertLetter(board,letter,pos):
    board[pos] = letter
def spaceIsFree(b,pos):
    return b[pos] == ' '
def isBoardFull(b):
    if b.count(' ') > 1:
        return False
    else:
        return True
#function to check the winner 
def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove(board):
    run = True
    while run:
        move = int(input("please select a position to enter the X between 1 to 9 :"))
        if move > 0 and move < 10:
            if spaceIsFree(board,move):
                run = False
                insertLetter(board,'X' , move)
            else:
                print('Sorry, this space is occupied')
        else:
            print('please type a number between 1 and 9')
def player2Move(board):
    run = True
    while run:
        move = int(input("please select a position to enter the O between 1 to 9 :"))
        if move > 0 and move < 10:
            if spaceIsFree(board,move):
                run = False
                insertLetter(board,'O' , move)
            else:
                print('Sorry, this space is occupied')
        else:
            print('please type a number between 1 and 9')

def computerMove(board):
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move=0
    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move
    if 5 in possibleMoves:
        move = 5
        return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
 
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    else:
        return move
#function to select random no. from a list 
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
def playagain():
        x=input('Do you want to play again(y/n): ')
        if x.lower()=='y':
            return True
        else:
            return False

print('************Tic-Tac-Toe Game************')
while True:
    #reset the board
    theboard=[' ' for x in range(10)]
    print('Select a mode')
    print('1.Single \n2.Multiplayer')
    mode=int(input('Enter your choice here :'))
    if mode>=3 or mode<1:
        print('Invalid choice...')
    if mode==1:
        printBoard(theboard)
        while True:
            if not(IsWinner(theboard,'O')):
                playerMove(theboard)
                printBoard(theboard)
            else:
                print('The computer has beaten you! You lose.')
                break
            if not(IsWinner(theboard,'X')):
                move=computerMove(theboard)
                if move==0:
                    break
                else:
                    insertLetter(theboard,'O',move)
                    print('computer placed an O on position' , move , ':')
                    printBoard(theboard)
            else :
                print('Hooray! You have won the game!')
                break
        if (isBoardFull(theboard) and not(IsWinner(theboard,'O')) and not(IsWinner(theboard,'X'))):
            print('The game is a tie')
    if mode==2:
        printBoard(theboard)
        while True:
            if not(IsWinner(theboard,'O')):
                playerMove(theboard)
                printBoard(theboard)
                if (isBoardFull(theboard) and not(IsWinner(theboard,'O')) and not(IsWinner(theboard,'X'))):
                    print('The game is a tie')
                    break
            else:
                print("'O' won the game")
                break
            if not(IsWinner(theboard,'X')):
                player2Move(theboard)
                printBoard(theboard)
            else:
                print("'X' won the game")
                break
    if not playagain():
        break
            