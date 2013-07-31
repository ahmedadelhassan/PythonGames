#Includes
from random import randint
from math import floor

##################################
## Global Variables and Defines ##
##################################
TURNS = 5
PROMPT_WIDTH = 80
BOARD_LENGTH = 5
BOARD_WIDTH = 5
NUM_OF_SHIPS = 2
REMAINING_SHIPS = NUM_OF_SHIPS
GAME_START = True
#-----------------------------------------------------------------------------------#
###############################
## Functions Defintions area ##
###############################

#Board Initialization Function
def InitBoard(rows, cols, ships):
    #Initialize size and shape of board
    board = []
    for index in range(rows):
        board.append(["~"] * cols)
    #Initialize ships in random locations on board
    #Define a list of tuples for ship locations
    ships_locations = []
    for index in range(ships):
        rand_row = randint(0, rows - 1)
        rand_col = randint(0, cols - 1)
        #Check if random location chosen before
        while ((rand_row, rand_col) in ships_locations == True):
            rand_row = randint(0, rows - 1)
            rand_col = randint(0, cols - 1)
        ships_locations.append((rand_row, rand_col))
    print (ships_locations)
    return board, ships_locations

#Game Welcome and Board Display Function
def DisplayBoard(board):
    #Display Initial Screen first time only
    global GAME_START
    if GAME_START == True:
        print(" ----------------------------------------------------------------")
        print("|                  Welcome to Battleship Game                    |")
        print(" ----------------------------------------------------------------")
        #Display Game guidlines for the player
        print("\n")
        print("You have " + str(TURNS) + " turns to guess the locations of the "
              + str(NUM_OF_SHIPS) + " ships hidden within the ocean")
        print("\nBe aware, the ocean coordinates start from (0, 0)")
        input("\nTo Start playing press Enter")
        GAME_START = False
    #Draw the board in the center of screen
    #Calculate the needed shift to draw board in the center
    global PROMPT_WIDTH, BOARD_LENGTH
    shift = floor((PROMPT_WIDTH - ((BOARD_LENGTH*2)-1))/2)
    print("\n")
    print(" ----------------------------------------------------------------")
    for row in board:
        print(" " * shift + " ".join(row) + " " * shift)
    print(" ----------------------------------------------------------------")
    

#User Input and Input Handling Function
def GuessShip():
    #Ask the player to enter two coordinates on the board
    guessed_row = input("\nGuess a row number: ")
    guessed_col = input("\nGuess a col number: ")
    #Check for correct input of positive or zero integers
    while guessed_row.isdecimal() == False or guessed_col.isdecimal() == False:
        print("\nPlease enter two positive or zero numbers")
        guessed_row = input("\nGuess a row number: ")
        guessed_col = input("\nGuess a col number: ")
    return (int(guessed_row), int(guessed_col))

#Input Checking and Results Function
def CheckGuess(guessed_location, ships_locations, board):
    global REMAINING_SHIPS
    #Check if guessed location contains a ship
    if (guessed_location in ships_locations) == True:
        print("\nGood Job!, You have destroyed a ship")
        REMAINING_SHIPS -= 1
        print("\n" + str(REMAINING_SHIPS) + " ships remaining")
        board[guessed_location[0]][guessed_location[1]] = "X"
        return board
    #Check if the guessed location is incorrect
    else:
        if guessed_location[0] > (len(board) - 1) or guessed_location[1] > (len(board[0])- 1):
            print("\nOops, that's not even in the ocean")
        elif board[guessed_location[0]][guessed_location[1]] == "X":
            print("\nYou already guessed that place!")
        else:
            print("\nYou missed the battleships!")
            board[guessed_location[0]][guessed_location[1]] = "X"
        return board
        
#-----------------------------------------------------------------------------------#
####################
## Main Game Body ##
####################

#Initialize the game board
board, ships_locations = InitBoard(BOARD_LENGTH, BOARD_WIDTH, NUM_OF_SHIPS)
DisplayBoard(board)
#Main turns loop
for turn in range(TURNS + 1):
    #Check for Game Over Condition
    if turn >= TURNS and REMAINING_SHIPS != 0:
        print("\nSorry you couldn't guess all the ships in " + str(TURNS) + " turns")
        print("\nGAME OVER!")
    
    #Display turn number
    print("\nTurn Number " + str(turn + 1))

    guessed_ship = GuessShip()

    board = CheckGuess(guessed_ship, ships_locations, board)

    DisplayBoard(board)

    #Check for win condition
    if REMAINING_SHIPS == 0:
        print("\nCongratulations! You have cleared this level")
        break
    #Wait for user input to continue
    input("\nPress Enter to continue")

print("\n\nTHANK YOU FOR PLAYING BATTLESHIP!")
