def cakes(recipe, available):
    r = [] 
    for k,v in recipe.items():
        if k in available and available.get(k) / v > 0:
           r.append(available.get(k) / v)
        else:
           r=[0]
           break
    r.sort()
    return int(r[0])
