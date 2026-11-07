def printer_error(s):
    errors = sum(1 for l in s if l not in 'abcdefghijklm')
    return f'{errors}/{len(s)}'