from bisect import bisect  # 1
n = int(input())
towns = sorted(enumerate(list(map(int, input().split()))), key=lambda x: x[1])
m = int(input())
bunkers = sorted(enumerate(list(map(int, input().split()))), key=lambda x: x[1])
indices = [None] * n
bunc = list(map(lambda x: x[1], bunkers))
for i in towns:
    ind = i[0]
    coor = i[1]
    bu = bisect(bunc, coor)
    if bu <= 0:
        indices[ind] = bunkers[0][0]
        continue
    elif bu == m:
        indices[ind] = bunkers[m - 1][0]
        continue
    buf = min(bunkers[bu], bunkers[bu - 1], key=lambda x: abs(x[1] - coor))
    indices[ind] = buf[0]
print(*(x + 1 for x in indices))
