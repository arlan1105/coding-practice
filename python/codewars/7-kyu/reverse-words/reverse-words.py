def reverse_words(text):
    return ' '.join([word[::-1] for word in text.replace(' ', '_').split('_')])