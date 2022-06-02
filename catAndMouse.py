def catAndMouse(x, y, z):
    dist1 = abs(z - x)
    dist2 = abs(z - y)
    if dist1 > dist2:
        return "Cat B"
    elif dist1 < dist2:
        return "Cat A"
    else:
        return "Mouse C"