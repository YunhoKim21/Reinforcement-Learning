#rules: policy: random move, the game terminates when it reaches to 0, 0 or 3, 3. Each moves gives -1 reward
import copy

valuefunction = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # the value function("how good the state is")
newvaluefunction = copy.deepcopy(valuefunction)
gamma = 0.5 # the discount factor 0: short sighted, 1: long sighted

for i in range(1000):
    print(i)
    valuefunction = copy.deepcopy(newvaluefunction)
    for row in range(4):
        for col in range(4):
            if row==0 and col==0:
                continue
            if row == 3 and col == 3:
                continue
            result = 0
            result += valuefunction[max(row-1, 0)][col]
            result += valuefunction[min(row+1, 3)][col]
            result += valuefunction[row][max(col-1, 0)]
            result += valuefunction[row][min(col+1, 3)]

            newvaluefunction[row][col] = gamma*result/4-1
    
    for row in newvaluefunction:
        for v in row:
            print(v, end = ' ')
        print()
    