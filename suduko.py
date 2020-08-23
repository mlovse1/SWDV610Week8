#Week 8 : Final Project
# Choose a problem that can be solved by utilizing algorithms and data structures
#  and implement them into a program.
#program to solve a sudoku puzzle
#9x9 grid subdivided into 3x3 mini-grids
#each mini-grid, column, and row each contains
#numbers 1-9 with no repeats per mini-grid, column, or row
#blank spaces in the puzzle are notated by a 0
#uses nested lists and backtracking



#function to print the puzzle
def printboard(board):
    #uses the length of the board for the size of the range
    for row in range(len(board)):
        #modulo operator and != 0 used to determine where to print the lines for
        #the puzzle to be displayed properly
        if row % 3 == 0 and row !=0:
            print("---------------")
        #for loop uses len(board[0]) (The first row) to determine where
        #to put the vertical markers
        for cols in range(len(board[0])):
            #modulu operator and != 0 used again to put lines in proper place
            if cols % 3 == 0 and cols != 0:
                print(" | ", end='')
            #if-else statements to print the rows and columns
            if cols == 8:
                print(board[row][cols])
            else:
                print(str(board[row][cols]) + '', end = '')
                
                 
#function to find the empty spaces on the board that are notated by a 0
def findEmptySpace(board):
    for rows in range(len(board)):
        for cols in range(len(board[0])):
            if board[rows][cols] == 0:
                return (rows, cols)         
    return None
#function to check if the number being placed is an allowed move
def valid(board, num, pos):
    #will check the row to see if valid
    for i in range(len(board[0])):
        if board[pos[0]][i]== num and pos[1] != i:
            return False
        
    #checks column to see if valid
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos [0] != i:
            return False
    
    #checks mini-grid
    boxX = pos[1] // 3
    boxY = pos[0] // 3
    #for loop that loops through to check each box 
    for i in range(boxY*3, boxY*3+3):
        for j in range(boxX * 3, boxX*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    
    return True

#function to solve the puzzle - uses backtracking
#Check if that number is valid in the current spot based on the current board
#If the number is valid, recursively attempts to fill the board 
#If the number is not valid, resets the square most recently filled
#and goes back to the last step.
def solve(board):
    
    findSol = findEmptySpace(board)
    #base case
    #if emptyspace is not found, the puzzle is solved
    if not findSol:
        return True
    
    else:
        row, col = findSol
        
    for i in range (1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board): #recursive call
                return True
            
            board[row][col] = 0
    return False

def main ():
    
#board is a set of nested lists
    b = [
        [0,0,0,0,0,7,6,5,0],
        [8,0,0,1,0,0,0,0,9],
        [0,7,0,0,2,0,0,0,0],
        [2,0,0,0,0,1,3,0,0],
        [5,0,0,0,0,0,0,0,1],
        [0,0,6,7,0,0,0,0,8],
        [0,0,0,0,6,0,0,9,0],
        [6,0,0,0,0,8,0,0,2],
        [0,3,8,5,0,0,0,0,0]
    ]

            
    print("Unsolved Puzzle: ")      
    printboard(b)
    solve(b)
    print()
    print("###############")
    print("Solution: ")
    printboard(b)

main()