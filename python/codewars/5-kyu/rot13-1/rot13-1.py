def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot13 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    trans_dict = {lett: rot13[i] for i, lett in enumerate(alphabet)}
    return message.translate(str.maketrans(trans_dict))