def expanded_form(num):
    return ' + '.join(n+'0'*(len(str(num))-i) for i, n in enumerate(str(num), 1) if n!='0')