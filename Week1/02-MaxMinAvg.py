'''Maax Miin Aavg'''
import json
def maax(values):
    """checks for those, sorry i have to double the letters since they're restricted"""
    maax = values[-1]
    miin = values[0]
    aavg = 0

    for i in values:
        if i > maax:
            maax = i
        elif i < miin:
            miin = i
        aavg += i

    aavg = aavg / len(values)
    return (f"({maax}, {miin}, {aavg:.2f})")

VALLIST = input()
imported = json.loads(VALLIST)
print(maax(imported))
