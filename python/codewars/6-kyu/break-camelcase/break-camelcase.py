def solution(s):
    return ''.join(' '+l if l.isupper() else l for i, l in enumerate(s))