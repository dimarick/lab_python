num = int(input())

if num <= 0:
    print("Неверный ввод")
    exit

bin = ''
oct = ''
hex = ''

n = num
while n > 0:
    bin = str(n % 2) + bin
    n //= 2

n = num
while n > 0:
    oct = str(n % 8) + oct
    n //= 8

n = num
while n > 0:
    d = n % 16
    hex = str(d) if d < 10 else chr(ord('A') + d - 10) + hex
    n //= 16

print(bin, oct, hex, sep=', ')
