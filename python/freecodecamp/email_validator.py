def validate(email):
    if email.count('@') != 1 or '..' in email:
        return False
        
    local, domain = email.split('@')
    tld = domain.split('.')[-1]
    
    if not local.replace('.', '').replace('-', '').replace('_', '').isalnum():
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '.' not in domain:
        return False
    if not(len(tld) >= 2 and tld.isalpha()):
        return False
    return True

print(validate("develop.ment_user@c0D!NG.R.CKS"))
print(validate("b@sh.c"))
