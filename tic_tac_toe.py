import random


# -----------------------------------
# DISPLAY THE BOARD
# -----------------------------------

def display_board(board):
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()


# -----------------------------------
# CHECK IF SOMEONE WON
# -----------------------------------

def check_winner(board, player):

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:

        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):

            return True

    return False


# -----------------------------------
# CHECK IF BOARD IS FULL
# -----------------------------------

def board_full(board):

    for space in board:

        if space != "X" and space != "O":
            return False

    return True


# -----------------------------------
# PLAYER MOVE
# -----------------------------------

def player_move(board):

    while True:

        try:
            move = int(input("Choose a space (1-9): "))
            move = move - 1

            # Make sure the number is valid
            if move < 0 or move > 8:
                print("Please choose a number from 1 to 9.")

            # Make sure the space isn't taken
            elif board[move] == "X" or board[move] == "O":
                print("That space is already taken!")

            else:
                board[move] = "X"
                break

        except ValueError:
            print("Please enter a number.")


# -----------------------------------
# COMPUTER MOVE
# -----------------------------------

def computer_move(board):

    available_spaces = []

    # Find all empty spaces
    for i in range(9):

        if board[i] != "X" and board[i] != "O":
            available_spaces.append(i)

    # Pick a random empty space
    move = random.choice(available_spaces)

    board[move] = "O"

    print("The computer chose space {}.".format(move + 1))


# -----------------------------------
# MAIN GAME
# -----------------------------------

def play_game():

    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    print("================================")
    print("        TIC TAC TOE")
    print("================================")

    print("\nYou are X.")
    print("The computer is O.")

    display_board(board)

    # Game loop
    while True:

        # ---------------------------
        # PLAYER'S TURN
        # ---------------------------

        print("YOUR TURN")

        player_move(board)

        display_board(board)

        # Check if player won
        if check_winner(board, "X"):
            print("YOU WIN!")
            break

        # Check if board is full
        if board_full(board):
            print("It's a draw!")
            break

        # ---------------------------
        # COMPUTER'S TURN
        # ---------------------------

        print("COMPUTER'S TURN")

        computer_move(board)

        display_board(board)

        # Check if computer won
        if check_winner(board, "O"):
            print("THE COMPUTER WINS!")
            break

        # Check if board is full
        if board_full(board):
            print("It's a draw!")
            break


# -----------------------------------
# START THE GAME
# -----------------------------------

play_game()