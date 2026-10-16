def substring_test(s1, s2):

    return any(s2[i:i+2].lower() in s1.lower() for i in range(len(s2)-1))

print(substring_test("Something", "Fun"))
print(substring_test("Something", "Home"))