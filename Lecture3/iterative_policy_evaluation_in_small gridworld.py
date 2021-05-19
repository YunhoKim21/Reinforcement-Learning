import copy 

valuefunction = [0 for i in range(16)]
            
newvaluefunction = [0 for i in range(16)]

reward = -1

for i in range(100):
    valuefunction = copy.deepcopy(newvaluefunction)
    
    for j in range(16):
        if j==0 or j==15:
            continue
        

    for j in range(16):
        if j==0 or j==15:
            continue
        valuefunction[j] += reward
        if j==1:
            newvaluefunction[j] = (valuefunction[0]+valuefunction[2]+valuefunction[5]+valuefunction[1])/4
        elif j==2:
            newvaluefunction[j] = (valuefunction[1]+valuefunction[6]+valuefunction[3]+valuefunction[2])/4
        elif j==3:
            newvaluefunction[j] = (valuefunction[2]+valuefunction[7]+valuefunction[3]+valuefunction[3])/4
        elif j==4:
            newvaluefunction[j] = (valuefunction[0]+valuefunction[5]+valuefunction[8]+valuefunction[4])/4
        elif j==7:
            newvaluefunction[j] = (valuefunction[3]+valuefunction[6]+valuefunction[11]+valuefunction[7])/4
        elif j==8:
            newvaluefunction[j] = (valuefunction[4]+valuefunction[9]+valuefunction[12]+valuefunction[8])/4
        elif j==11:
            newvaluefunction[j] = (valuefunction[7]+valuefunction[10]+valuefunction[13]+valuefunction[11])/4
        elif j==12:
            newvaluefunction[j] = (valuefunction[8]+valuefunction[13]+valuefunction[12]+valuefunction[12])/4
        elif j==13:
            newvaluefunction[j] = (valuefunction[9]+valuefunction[12]+valuefunction[14]+valuefunction[13])/4
        elif j==14:
            newvaluefunction[j] = (valuefunction[10]+valuefunction[13]+valuefunction[15]+valuefunction[14])/4
        else:
            newvaluefunction[j] = (valuefunction[j+1]+valuefunction[j-1]+valuefunction[j-4]+valuefunction[j+4])/4
        
    

    print(newvaluefunction)
            