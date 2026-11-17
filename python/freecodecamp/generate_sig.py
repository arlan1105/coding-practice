def generate_signature(name, title, company):

    if ord(name[0].upper()) < 73: prefix = '>>' 
    elif ord(name[0].upper()) < 82: prefix = '--' 
    else: prefix = '::'
    
    return prefix + f'{name}, {title} at {company}'
        

print(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"))
