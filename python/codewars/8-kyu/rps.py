def rps(p1, p2):
    beats = { 'rock' : 'paper', 'paper' : 'scissors', 'scissors' : 'rock'}
    if p1 == p2: return 'Draw!'
    elif beats[p1] == p2: return "Player 2 won!"
    return "Player 1 won!"
