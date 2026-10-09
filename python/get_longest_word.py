def get_longest_word(sentence):

    str_list = sentence.replace('.', '').split()
    lengths = []
    for word in str_list:
        lengths.append(len(word))
    
    longest = lengths.index(max(lengths))

    return str_list[longest]

print(get_longest_word("Coding challenges are fun and educational."))