n = int(input())
lp = []
rp = []
for __ in range(n):
    inp = list(map(int, input().split()))
    lp.append(inp[0])
    rp.append(inp[1])
lp.sort()
rp.sort()
for i in points:
    print(bisect(lp, i) - bisect_left(rp, i))
