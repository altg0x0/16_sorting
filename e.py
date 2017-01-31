n = int(input())
arr = list(map(int, input().split()))
ch = 0
changed = True
while changed:
    changed = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            changed = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            ch += 1
print(ch)
