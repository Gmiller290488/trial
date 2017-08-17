def boggle_checker(board, guess):
    positions = []
    for row in board:
        print(row)
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == guess[0]:
                positions.append([x, y])

    for position in positions:
        x = position[0]
        y = position[1]
        a = checkLetter(getAdjPositions(x, y), board, 1, guess, board[x][y])
        if a == True:
            return True
    return False


def getAdjPositions(x, y):
    adjPos = []
    adjPos.append([x - 1, y])
    adjPos.append([x - 1, y - 1])
    adjPos.append([x - 1, y + 1])
    adjPos.append([x, y - 1])
    adjPos.append([x, y + 1])
    adjPos.append([+1, y - 1])
    adjPos.append([x + 1, y])
    adjPos.append([x + 1, y + 1])
    return adjPos


def checkLetter(position, board, count, guess, curr_word):
    for item in position:
        if item[0] >= 0 and item[0] <= 3 and item[1] >= 0 and item[1] <= 3:
            x = item[0]
            y = item[1]
            if board[x][y] == guess[count]:
                print("Found letter number: ", count, "-", guess[count], "at position (", x, ",", y, ")")
                curr_word += guess[count]
                board[x][y] = "x"
                if count + 1 < len(guess):
                    count += 1
                    return checkLetter(getAdjPositions(x, y), board, count, guess, curr_word)
                else:
                    print(curr_word)
                    return True



guess1 = "ISRL"
board1 = [["I", "L", "A", "W"], ["B", "N", "G", "E"], ["I", "U", "A", "O"], ["A", "S", "R", "L"]]
print(boggle_checker(board1, guess1))