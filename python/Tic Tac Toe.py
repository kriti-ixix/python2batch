# Importing the libraries
import os

# Global variables
theBoard = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

def clearScreen():
	if os.name == 'posix':
		#For UNIX system 'posix':
		_ = os.system('clear')
	else:
		#For Windows system 'nt':
		_ = os.system('cls')

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
            print("The game ends in a draw")
            break

        move = input("Enter your move {}: ".format(turn))

        if move not in theBoard.keys():
            print("Invalid move")
            continue

        #If the place is empty
        if theBoard[move] == ' ':
            theBoard[move] = turn

            #Checking if we have a winner
            winner = checkWin(turn)
            if winner != '':
                printBoard(theBoard)
                print("Congratulations! The winner is", turn)
                break

            else:
                count += 1
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

        else:
            print("Sorry that place is already filled")
            continue

def checkWin(turn):
    winner = ''

    #Checking rows
    if (theBoard['7']==theBoard['8']==theBoard['9']==turn) or (theBoard['4']==theBoard['5']==theBoard['6']==turn) or (theBoard['1']==theBoard['2']==theBoard['3']==turn):
        winner = turn

    #Checking columns
    if (theBoard['7']==theBoard['4']==theBoard['1']==turn) or (theBoard['8']==theBoard['5']==theBoard['2']==turn) or (theBoard['9']==theBoard['6']==theBoard['3']==turn):
        winner = turn

    #Checking diagonals
    if (theBoard['7']==theBoard['5']==theBoard['3']==turn) or (theBoard['9']==theBoard['5']==theBoard['1']==turn):
        winner = turn

    return winner #Value can be '', 'X', 'O'

def restartGame():
    choice = input("Would you like to play again? (Y/N): ")
    if choice.lower() == 'y':
        for values in theBoard:
            theBoard[values] = ' '
        clearScreen()
        main()
    else:
        print("Thank you for playing!")

# Main function
def main():
    playGame()
    restartGame()

if __name__ == '__main__':
    main()
