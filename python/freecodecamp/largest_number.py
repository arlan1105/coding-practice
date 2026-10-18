import re
def largest_number(s):
    
    return max([float(x) for x in re.sub(r"[,!?:;]", ' ', s).split()])

print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))