"""Graphics"""

# enumerations of color profiles
OneWeb = 0
Telesat = 1

def profile(n):
    """Return the rgb color string associated with given profile."""

    if n == 0:
        color = '00FFFF'
    elif n == 1:
        color = 'FF00FF'
    elif n == 2:
        color = 'FFFF00'
    else:
        color = 'FFFFFF'
    return color

def colorProfile(n):
    """Return the integer color code associated with given profile."""

    return hexColorToInt(profile(n))

def hexColorToInt(rgb):
    """Convert rgb color string to STK integer color code."""

    r = int(rgb[0:2],16)
    g = int(rgb[2:4],16)
    b = int(rgb[4:6],16)

    color = format(b, '02X') + format(g, '02X') + format(r, '02X')

    return int(color,16) # STK uses BGR color codes
