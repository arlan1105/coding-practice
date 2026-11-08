def can_post(message):
    if len(message) <= 80: return 'long post' if len(message) > 40 else 'short post'
    return 'invalid post'
