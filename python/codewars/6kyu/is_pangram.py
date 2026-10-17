import string

def is_pangram(st):
    return set(string.ascii_lowercase).issubset(set(st.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog."))