from bisect import bisect, bisect_left
l, n, m = map(int, input().split())
lp = []
rp = []
points = []
for __ in range(n):
    inp = list(map(int, input().split()))
    lp.append(inp[0])
    rp.append(inp[1])
for __ in range(m):
    points.append(int(input()))
lp.sort()
rp.sort()
for i in points:
    print(bisect(lp, i) - bisect_left(rp, i))
