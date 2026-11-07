def score(dice):
    total = 0
    if dice.count(1) == 3:
        total+=1000
    if dice.count(1) == 4:
        total+=1100
    if dice.count(1) == 5:
        total+=1200
    if dice.count(5) == 3:
        total+=500
    if dice.count(5) == 4:
        total+=550
    if dice.count(5) == 5:
        total+=600
    if dice.count(6) >= 3:
        total+=600
    if dice.count(4) >= 3:
        total+=400
    if dice.count(3) >= 3:
        total+=300
    if dice.count(2) >= 3:
        total+=200
    if dice.count(5) == 2:
        total+=100
    if dice.count(5) == 1:
        total+=50
    if dice.count(1) == 2:
        total+=200
    if dice.count(1) == 1:
        total+=100
    
    return total
​