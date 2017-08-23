import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def boggle_checker(board, guess):

    x = -1
    y = -1
    curr_word = ""
    count = 0

    # to visualise the board and word we are looking for
    print(guess)
    for row in board:
        print(row)

    a = checkLetter(get_adj_positions(x, y, len(board)), board, count, guess, curr_word)
    if a == True:
        return True
    return False


def board_marker(board, x, y):
    """" Mark the position found with an x so it can't be checked twice """

    board[x][y] = "x"
    return board


def get_adj_positions(x, y, max):
    """" Return all legal positions adjoining the x, y coordinate given"""

    adj_pos = []
    if (x or y == -1):
        x = 0
        y = 0
        for x, y in [(x + i, y + j) for i in range(0, max) for j in range(0, max)]:
            adj_pos.append([x, y])
        print(adj_pos)
        return adj_pos
    else:
        # Generate all coordinates of all squares surrounding given position
        for x, y in [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
            adj_pos.append([x, y])
        # Remove any coordinates that are not on the board
        adj_pos = list(filter(lambda x_y: -1 < x_y[0] < max and -1 < x_y[1] < max, adj_pos))
        return adj_pos


def checkLetter(position, board, count, guess, curr_word):
    """ Once all adjacent tiles are located, this checks to see if any of them tiles contain the next letter we need.
    If the next letter exists in the adjacent tiles, but that isn't the end of the word then the function is called again """

    # check each adjacent tile
    for item in position:
        x = item[0]
        y = item[1]
        print("Looking for " + (guess[count]))
        if board[x][y] == guess[count]:
            # add the letter found to our current word variable
            curr_word += guess[count]
            if count + 1 < len(guess):
                # call this function again with updated variables
                print("the current word is: " + curr_word)
                print("count is " + str(count+1) + "and length of guess is " + str(len(guess)))
                return checkLetter(get_adj_positions(x, y, len(board)), board_marker(board, x, y), count+1, guess, curr_word)
            else:
                # word is found, return True to exit function
                print(curr_word)
                return True


def board_generate():
    """" Random board generator for testing purposes"""

    board_size = random.randint(3, 7)
    board = [[alphabet[random.randint(0, 25)] for a in range(board_size)] for b in range(board_size)]
    return(board)


def guess_generate():
    """" Generate a random string for testing purposes"""

    guess = ""
    length = random.randint(2,3)
    for i in range(length):
        guess += alphabet[random.randint(0, 25)]
    return guess


for i in range(1):
     print(boggle_checker([ ["I","L", "I"],["C","N", "I"], ["C", "D", "L"] ], "IL"))