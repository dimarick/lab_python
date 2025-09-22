print('yes' if (lambda x: x.count('1') == len(x) // 2 and len(x) % 2 == 0)(input()) else 'no')
