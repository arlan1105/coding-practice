# freeCodeCamp Daily Challenge: Spam Number Checker
#
# Input: a phone number string like "+A (BBB) CCC-DDDD"
#   A   = country code (any length)
#   BBB = area code (3 digits)
#   CCC = first part of local number (3 digits)
#   DDDD = last part of local number (4 digits)
#
# Return True if the number is spam, False otherwise.
# Spam if ANY of these is true:
#   1. Country code is longer than 2 digits, or doesn't start with 0
#   2. Area code is above 900 or below 200
#   3. The sum of the 3 digits in CCC appears inside DDDD
#   4. Any digit repeats 4+ times in a row (formatting characters ignored)
#
# Note: the rules are made up for the puzzle

import re
def is_spam(number):

    numlist = [word.strip() for word in re.split(r'[-()+]', number) if word.strip()]
    numjoined = ''.join(numlist)

    return (len(numlist[0]) > 2 or not numlist[0].startswith('0')
        or int(numlist[1]) < 200 or int(numlist[1]) > 900
        or numlist[3].count(str(sum([int(digit) for digit in numlist[2]]))) > 0
        or any(a == b == c == d for a, b, c, d in zip(numjoined, numjoined[1:], numjoined[2:], numjoined[3:])))

print(f'+0 (200) 234-0182', is_spam('+0 (200) 234-0182'))
print(f'+1 (300) 234-0182 violates r1', is_spam('+1 (300) 234-0182'))
print(f'+0 (955) 234-4364 violates r2', is_spam('+0 (955) 234-4364'))
print(f'+0 (555) 135-0192 violates r3', is_spam('+0 (555) 135-0192'))
print(f'+0 (555) 564-1987 violates r4', is_spam('+0 (555) 564-1987'))

