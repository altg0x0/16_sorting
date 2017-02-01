from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
c = Counter()
mi = min(arr)
ma = max(arr)
for i in arr:
    c[i] += 1
arr = []
for el in range(mi, ma + 1):
    arr += [el] * c[el]
print(*arr)
