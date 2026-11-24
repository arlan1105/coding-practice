def reverse_vowels(s):
    reverse = iter([l for l in s[::-1] if l.lower() in 'aeiou'])
    return ''.join(next(reverse) if l.lower() in 'aeiou' else l for l in s)