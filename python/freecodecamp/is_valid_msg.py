def is_valid_message(message, validation):

    return all(w[0].lower() == l for w, l in zip(message.split(), validation.lower())) and len(validation) == len(message.split())

print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))
