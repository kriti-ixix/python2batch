# Importing the libraries

# Global variables
theBoard = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

# User defined functions
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def playGame():
    turn = 'X' #Current turn 
    count = 0 #Numbers of turns played

    while True:
        printBoard(theBoard)

        if count == 9:
            break

        move = input("Enter your move: ")

        if move not in theBoard.keys():
            print("Invalid move")
            continue

        #If the place is empty
        if theBoard[move] == ' ':
            theBoard[move] = turn

            #Checking if we have a winner
            winner = checkWin(turn)

        else:
            print("Sorry that place is already filled")
            continue

def checkWin(turn):
    winner = ''

    #Checking rows
    if (theBoard['7']==theBoard['8']==theBoard['9']==turn) or (theBoard['4']==theBoard['5']==theBoard['6']==turn) or (theBoard['1']==theBoard['2']==theBoard['3']==turn):
        winner = turn

    #Checking columns

    #Checking diagonals

    return winner #Value can be '', 'X', 'O'
        
# Main function
playGame()