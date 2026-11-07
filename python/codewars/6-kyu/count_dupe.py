def duplicate_count(text):
    return len([lett for lett in set(text.lower()) if text.lower().count(lett) > 1])

print(duplicate_count('abcde'))
print(duplicate_count('wnbTRI5381fVjkvvfrab0r8ES5AKap7HRzqswEXROuihERrj0'))