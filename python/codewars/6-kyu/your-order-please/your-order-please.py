def order(sentence):
    digits = [lett for word in sentence.split() for lett in word if lett.isdigit()]
    return ' '.join(substr[1] for substr in sorted(zip(digits, sentence.split())))