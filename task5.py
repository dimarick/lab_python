input = input()

a = [0] * 2

for c in input:
    i = int(c)
    a[i] += 1

print("yes" if a[0] == a[1] else "no")
