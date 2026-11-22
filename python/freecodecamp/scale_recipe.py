def scale_recipe(ingredients, scale): 
    amt = [n.split() for n in ingredients]
    return [f'{float(n[0])*scale:g} ' + ' '.join(n[1:]) for n in amt]

print(scale_recipe(["2 C Flour", "1.5 T Sugar"], 2))
print(scale_recipe(["3 C Milk", "2 C Oats"], 0.5))
