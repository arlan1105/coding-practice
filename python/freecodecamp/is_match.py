def is_match(fingerprint_a, fingerprint_b):

    return len(fingerprint_a) == len(fingerprint_b) and sum(1 for a,b in zip(fingerprint_a, fingerprint_b) if a!=b)*10 <= len(fingerprint_a)

print(is_match("helloworld", "jelloworlds"))
