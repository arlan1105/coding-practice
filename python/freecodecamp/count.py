def count(text, parameter):
    ctr = 0 
    while len(text) != 0:
        if parameter == text[0:len(parameter)]:
            ctr +=1
        text = text[1:]
    return ctr

print(count('101010101010101010101', '101'))

# return sum(text.startswith(pattern, i) for i in range(len(text)))