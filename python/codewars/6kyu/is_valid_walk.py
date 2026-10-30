def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))