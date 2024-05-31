r,c = input().split()

c = int(c)
r = int(r)

if c <= 10:
    print(f'right' , 11 - r, c)
else:
    print(f'left', 11 - r, 21 - c)