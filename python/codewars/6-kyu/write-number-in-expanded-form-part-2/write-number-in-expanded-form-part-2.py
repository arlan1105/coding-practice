def expanded_form(num):
    whole, dec = str(num).split('.')
    whole = [n+'0'*(len(whole)-i) for i, n in enumerate(whole, 1) if n!='0'] 
    dec = [n + '/1' + '0'*i for i, n in enumerate(dec, 1) if n != '0']
    return ' + '.join(whole+dec)