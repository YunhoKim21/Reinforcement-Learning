import copy

def greedy(valuefunction, pos): #returns the "best" move, refer to the given value funciton
    bestoption = [0, 0]
    bestvalue = -10000000
    options = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    values = []
    for option in options:
        if pos[0]+option[0]>=0 and pos[0]+option[0]<4 and pos[1]+option[1]>=0 and pos[1]+option[1]<4:
            value = valuefunction[pos[0]+option[0]][pos[1]+option[1]]
            values.append(value)
        else:
            values.append(None)
        
    ret = []
    maxval = -1000
    for value in values:
        if value is not None:
            if value>maxval:
                maxval = value
    for i in range(4):
        if values[i] == maxval:
            ret.append(options[i])
    return ret

valuefunction = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # the value function("how good the state is")
gamma = 1 # the discount factor 0: short sighted, 1: long sighted

for i in range(10):
    print(i)
    valuefunction = copy.deepcopy(valuefunction)
    for row in range(4):
        for col in range(4):
            if row==0 and col==0:
                continue
            if row == 3 and col == 3:
                continue
            result = 0

            moves = greedy(valuefunction, [row, col]) # greedy policy is updated every iteration

            for move in moves:
                result += valuefunction[row+move[0]][col+move[1]]

            valuefunction[row][col] = gamma*result/len(moves)-1
    
    for row in valuefunction:
        for v in row:
            print(v, end = ' ')
        print()
