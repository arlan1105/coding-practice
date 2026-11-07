from preloaded import MORSE_CODE

def decode_morse(morse_code):
    return ''.join([' ' if l == '_space_' else MORSE_CODE[l] for l in morse_code.replace('   ', ' _space_ ').split()]).strip()
