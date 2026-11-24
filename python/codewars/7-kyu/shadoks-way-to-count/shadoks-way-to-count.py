import numpy as np
​
def shadok(n:int) -> str:
    lang = str.maketrans({'0':'GA', '1':'BU', '2':'ZO', '3':'MEU'})
    return np.base_repr(n, 4).translate(lang)