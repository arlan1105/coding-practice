def has_exoplanet(readings):
    lookup = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    luminosity = []

    for char in readings:
        level = lookup.index(char)
        luminosity.append(level)
    
    average = (sum(luminosity)/len(luminosity))
    ave80 = average * 0.8
    
    return any(x <= ave80 for x in luminosity)
    
print(has_exoplanet("FGFFCFFGG"))