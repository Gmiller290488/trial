import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def boggle_checker(board, guess):
    """"Return true is guess is a word on the board"""

    count = 0
    positions = []

    # to visualise the board
    print(guess)
    for row in board:
        print(row)


    """ Try turning this into a lambda function"""
    for x in range(len(board)):
        for y in range(len(board)):
            # if the first letter of the guess is found, save the position
            if board[x][y] == guess[count]:
                positions.append([x, y])
                print("Letter found at ", x, ", ", y)
    # if the first letter was found increment count
    # count is used as index for which letter in guess we are searching for
    if positions != []:
        count+=1
    else:
    #if the first letter isn't found, return False
        return False
    # for each position found run the function to look for next letter in adjoining tiles
    for position in positions:
        x = position[0]
        y = position[1]
        # Mark the first letter so that it can't be used again
        board[x][y] = "x"
        a = checkLetter(get_adj_positions(x, y, len(board)), board, count, guess, guess[0])
        if a == True:
            return True
    return False


def get_adj_positions(x, y, max):


    """" Return all legal positions adjoining the x, y coordinate given"""
    adj_pos = []
    # Generate all coordinates of all squares surrounding given position
    for x, y in [(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
        adj_pos.append([x, y])
    # Remove any coordinates that are not on the board
    adj_pos = list(filter(lambda x_y: -1 < x_y[0] < max and -1 < x_y[1] < max, adj_pos))
    return adj_pos


def checkLetter(position, board, count, guess, curr_word):
    for item in position:
        x = item[0]
        y = item[1]
        if board[x][y] == guess[count]:
            print("Letter found at ", x,", ", y)
            # add the letter found to our current word variable
            curr_word += guess[count]
            # mark the position so it can't be used again
            board[x][y] = "x"
            if count + 1 < len(guess):
                count += 1
                # call this function again with updated variables
                checkLetter(get_adj_positions(x, y, len(board)), board, count, guess, curr_word)
            else:
                # word is found, return True to exit function
                print(curr_word)
                return True

def board_generate():
    """" Random board generator for testing purposes"""
    board_size = random.randint(3, size)

    rows = ""
    for i in range(board_size):
        rows += " "
        for i in range(board_size):
            rows += (alphabet[random.randint(0, 25)])
    rows = rows.split()
    board = list(map(list, rows))
    return(board)

def guess_generate():
    """" Generate a random string for testing purposes"""
    guess = ""
    length = random.randint(2,3)
    for i in range(length):
        guess += alphabet[random.randint(0, 25)]
    return guess



# for i in range(100):
#     print(boggle_checker(board_generate(5), guess_generate()))
