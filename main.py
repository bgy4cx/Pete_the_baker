def cakes(recipe, available):
    r = [(available.get(k) / v) for k,v in recipe.items() if k in available and available.get(k) / v > 0]
    if len(r) != len(recipe):
        r=[0]
    r.sort()
    return int(r[0])
