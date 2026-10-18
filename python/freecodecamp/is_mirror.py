def is_mirror(str1, str2):
    str2 = ''.join([l for l in str2 if l.isalpha()])
    str1 = ''.join([l for l in str1 if l.isalpha()])
    return str1[::-1] == str2

print(is_mirror("helloworld", "helloworld"))
print(is_mirror("Hello World", "dlroW-olleH"))