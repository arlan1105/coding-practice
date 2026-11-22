def cakes(recipe, available):
    return min(available[ing]//recipe[ing] if ing in available else 0 for ing in recipe.keys())