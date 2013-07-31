from random import randint

board = []
NUM_OF_SHIPS = 5
REMAINING_SHIPS = NUM_OF_SHIPS
MAX_TURNS_PER_LEVEL = 7

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

ship_row = []
ship_col = []

def check_row(row):
    for i in ship_row:
        if row == i:
            return False
        else:
            return True

def check_col(col):
    for i in ship_col:
        if col == i:
            return False
        else:
            return True

def random_row(board):
    row = randint(0, len(board) - 1)
    while check_row(row) == False:
        row = randint(0, len(board) - 1)
    return row

def random_col(board):
    col = randint(0, len(board[0]) - 1)
    while check_col(col) == False:
        col = randint(0, len(board[0]) - 1)
    return col

for i in range(NUM_OF_SHIPS):
    ship_row.append(random_row(board)) 
    ship_col.append(random_col(board))

print (ship_row)
print (ship_col)

turn = 0
guessed_ships = []
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(MAX_TURNS_PER_LEVEL):
    # Print (turn + 1) here!
    print ("============================================================")
    print ("Turn Number " + str(turn + 1))

    guess_row = input("\nGuess Ship Row: ")
    guess_col = input("Guess Ship Col: ")
    
    while guess_row.isdigit() == False or guess_col.isdigit() == False:
        print ("Please enter two positive numbers")
        guess_row = input("Guess Ship Row: ")
        guess_col = input("Guess Ship Col: ")

    guess_row = int(guess_row)
    guess_col = int(guess_col)
        
    for i in range(NUM_OF_SHIPS):

        if (i in guessed_ships) == True:
            continue
    
        if guess_row == ship_row[i] and guess_col == ship_col[i]:
            print ("Good Job! You sunk my battleship " + str(i+1))
            board[guess_row][guess_col] = "X"
            REMAINING_SHIPS -= 1
            guessed_ships.append(i)
            break
        else:
            if (guess_row < 0 or guess_row > len(board)-1) or (guess_col < 0 or guess_col > len(board[0])-1):
                print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already.")
            else:
                print ("You missed my battleships")
                board[guess_row][guess_col] = "X"
            break

    print ("\nHere is how the sea looks now")
    print_board(board)

    if REMAINING_SHIPS == 0:
        print ("\nCongratulations! Level 1 Cleared!")
        break

    turn += 1
    if turn > MAX_TURNS_PER_LEVEL - 1:
        print ("\n============================================================")
        print ("Game Over")
        break
    
    input("Press Enter to continue to next turn")


# TEST WHEN A WRONG GUESS IS INPUT AFTER RIGHT ONE(S)
