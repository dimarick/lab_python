def parseInput(sep):
    i = 0

    a = []

    inValue = False

    for c in input():
        if c not in sep:
            if i >= len(a):
                a.append('')
            a[i] += c
            inValue = True
        else:
            if inValue:
                i += 1
                inValue = False

    return a
