n = int(input())
points = []
for __ in range(n):
    inp = list(map(int, input().split()))
    points.append((inp[0], 1))
    points.append((inp[1], -1))
points.sort()
pgen = (i for i in points)
seg = 0
p = 0
col = 0
for __ in range(2 * n):
    x = next(pgen)
    pnew = x[0]
    col += (pnew - p) if seg > 0 else 0
    seg += x[1]
    p = pnew
print(col)
