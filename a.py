n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    j = min(range(i, n), key=lambda x: arr[x])
    arr[i], arr[j] = arr[j], arr[i]
print(*arr)
