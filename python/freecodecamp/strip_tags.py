import re
def strip_tags(html):
    return re.sub(r'<[^>]+>', '', html)

print(strip_tags('<p class="center">Hello <b>World</b>!</p>'))