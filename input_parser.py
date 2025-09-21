def parseInput(sep=None):
    i = 0

    a = []

    inValue = False

    for c in input():
        if (sep is not None and c not in sep) or (sep is None and (c.isdigit() or c == '-' or c == '.')):
            if i >= len(a):
                a.append('')
            a[i] += c
            inValue = True
        else:
            if inValue:
                i += 1
                inValue = False

    return a
