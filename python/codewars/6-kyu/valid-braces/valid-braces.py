def valid_braces(string):
    while '[]' in string or '()' in string or '{}' in string:
        string = string.replace('{}', '')
        string = string.replace('()', '')
        string = string.replace('[]', '')
    return string == ''
​