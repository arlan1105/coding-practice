def cakes(recipe, available):
    return min(available.get(ing,0)//recipe[ing] for ing in recipe.keys())