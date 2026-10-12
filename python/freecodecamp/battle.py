def battle(our_team, opponent):
    def value(side):
        return [sum(ord(c)-96 if c.islower() else (ord(c)-64)*2  for c in word) for word in our_team.split(' ')]

    wins = 0
    for team, opp in zip(value(our_team), value(opponent)):
        if team > opp: wins +=1 
        elif opp > team: wins -=1

    if wins == 0: return 'Draw'
    elif wins > 0: return 'We win'
    else: return 'We lose'

print(battle("hello world", "hello word"))