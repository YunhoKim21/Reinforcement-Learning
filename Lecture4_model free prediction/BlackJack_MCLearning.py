import random
def drawCard():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

limit = 20

def policy(mynumber):
    if mynumber>=limit:
        return "stick"
    return "twist"

def play():
    bent = []
    agent = 0
    dealer = 0
    dealer += (drawCard()+drawCard())
    while agent < 12:
        agent += drawCard()

    while policy(agent)=="twist":
        bent.append(agent)

        agent += drawCard()
        if agent>21:
            return -1, bent, dealer
    
    if agent > dealer:
        return 1, bent, dealer
    if agent == dealer:
        return 0, bent, dealer
    return -1, bent, dealer

valuefunction = [[[0, 0] for agent in range(10)] for dealer in range(21)]

for trial in range(100000):
    reward, bent, dealer = play()
    for state in bent:
        valuefunction[dealer][state-12][0] += 1
        valuefunction[dealer][state-12][1] += reward
    
for i in valuefunction:
    for j in i:
        if j[0]!=0:
            print(j[1]/j[0], end = '')
        else:
            print('zero')
    print()