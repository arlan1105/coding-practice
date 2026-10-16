def spin_words(sentence):
    return ' '.join(words[::-1] if len(words) >= 5 else words for words in sentence.split())
    
print(spin_words("Hey fellow warriors"))

# def spin_words(sentence):
#     sentence = sentence.split()
#     for i, words in enumerate(sentence):
#         if len(words) >= 5:
#             sentence[i] = words[::-1]
#     return ' '.join(sentence)