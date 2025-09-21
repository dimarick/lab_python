from input_parser import parseInput
a = parseInput(sep=' ')

b = ""
for i in a:
    b += i[-1]

print(b)
