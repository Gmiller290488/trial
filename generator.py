# import random
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# board = []
# board_size = random.randint(3, 8)
# print(alphabet[random.randint(0, 25)])
# rows = ""
# for i in range(board_size):
#     rows += " "
#     for i in range(board_size):
#         rows+=(alphabet[random.randint(0, 25)])
# rows = rows.split( )
# board = list(map(list, rows))
# print(board)

def getPos(x, y, max):
    result = []
    for x,y in [(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        result.append([x, y])
    print(result)
    result = list(filter(lambda x_y: x_y[0] > -1 and x_y[1] > -1 and x_y[0] <= max and x_y[1] <= max, result))
    print(result)
    #result = filter(lambda (x, y): x > 0 and y > 0, result)
    #print(result)

getPos(3,0,3)