n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
indices = sorted(range(n), key=lambda x: arr[x])
print(*indices)
