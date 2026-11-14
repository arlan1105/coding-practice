def get_grade(s1, s2, s3):
    # Code here
    avg = (s1+s2+s3)/3
    if avg < 60: return 'F'
    elif avg < 70: return 'D'
    elif avg < 80: return 'C'
    elif avg < 90: return 'B'
    return 'A'
    
    