def verify(message, key, signature):

    return sum(ord(l)-96 if l.islower() else ord(l)-38 for l in message+key if l.isalpha()) == signature

print(verify("freeCodeCamp", "Rocks", 238))