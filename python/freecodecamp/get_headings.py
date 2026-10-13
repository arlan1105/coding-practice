def get_headings(csv):
    return [word.strip() for word in csv.split(',')]

print(get_headings("username , email , signup date "))