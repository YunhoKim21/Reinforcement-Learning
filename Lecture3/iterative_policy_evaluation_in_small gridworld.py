import copy

valuefunction = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
newvaluefunction = copy.deepcopy(valuefunction)


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

            newvaluefunction[row][col] = result/4-1
    
    for row in newvaluefunction:
        for v in row:
            print(v, end = ' ')
        print()
    