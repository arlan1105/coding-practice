def is_isogram(string):
    string = string.lower()
    return not any(string[i] in string[i+1:] for i in range(len(string)))
        
print(is_isogram('Dermatogylphics'))
print(is_isogram('aba'))

#return len(string) == len(set(string.lower()))