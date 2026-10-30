def sort(emails):
    def key(email):
        user, domain = email.lower().split('@')
        return (domain, user)
    return sorted(emails, key=key)
    
print(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))