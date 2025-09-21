from input_parser import parseInput

a = parseInput()

print(round(float(a[0]) ** 2, 2), ", ", round(float(a[0]) * 4, 2), ", ", round(float(a[0]) * 2 ** 0.5, 2), sep="")
