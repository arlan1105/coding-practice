def find_short(s):
    return min(len(w) for w in s.split())
        
print(find_short("bitcoin take over the world maybe who knows perhaps"))