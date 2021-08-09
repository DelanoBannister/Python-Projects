import time

winner = False
height =  6
width = 7
wturn = 2
last = 0
column = 0

def gboard( height, width):
    for i in range(8):
        if i < height:
            board.append(["_"] * width)
        elif i < width:
            board.append(["^"] * width)
        else:
            for h in range(width):
                xaxis.append(str(h+1))
            board.append(xaxis)
            
def playground(board):
    print ("\n")
    for row in board:
        print(" ".join(row))
    print ("\n")

def main():
    print ("Welcome to Connect Four!")
    
        
def start():
    while True:
            column = int(input("Pick a column (1-7): ")) -1
            row = int(input("Pick a row (1-6):")) -1
            if column >= 0 and column <= width:
                if row >=0 and row <= height:
                    for i in range(7):
                        if board[row][column] == ("_"):
                            last = row
                            score(last, column)
            else:
                print("Not a valid number! Please try again...")
            break
def score(last, column):
    if wturn == 2:
        board[last][column] = ("X")
    else:
        board[last][column] = ("O")
    playground(board)

def player(turn):
    if turn == 2 :
        turn= 1
        print ("It is player %s's turn." % turn)
        return turn
    elif turn == 1:
        turn= 2
        print ("It is player %s's turn." % turn)
        return turn

def check_winner(board, player):
    #check horizontal spaces
    for y in range(height):
        for x in range(width - 3):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True

    #check vertical spaces
    for x in range(width):
        for y in range(height - 3):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                return True

    #check / diagonal spaces
    for x in range(width - 3):
        for y in range(3, height):
            if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True

    #check \ diagonal spaces
    for x in range(width - 3):
        for y in range(height - 3):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True

    return False


xaxis=[]
board=[]

main()
gboard(height,width)
playground(board)
while winner == False:
    wturn = player(wturn)
    start()
    winner = check_winner(board, str(wturn))
    