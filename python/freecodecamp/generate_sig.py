def generate_signature(name, title, company):

    first = name[0].upper()
    prefix = '>>' if first <= 'I' else '--' if first <= 'R' else '::'
    return prefix + f'{name}, {title} at {company}'
        
print(generate_signature("Quinn Waverly", "Founder and CEO", "TechCo"))
