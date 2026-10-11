def filter_list(l):
    return [d for d in l if not isinstance(d, str)]
    
print(filter_list([1,2,'aasf','1','123',123]))