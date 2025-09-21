from input_parser import parseInput
a = parseInput()

for i in range(len(a)):
    a[i] = int(a[i])

# Bubble sort
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a[1])
