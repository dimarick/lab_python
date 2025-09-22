filtered = ''
for c in input():
    if c.isdigit() or c == '+':
        filtered += c

print(filtered)