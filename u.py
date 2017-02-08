n, a = map(int, input().split())
arr = []
for __ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
solved = 0
for i in range(n):
    if arr[i][0] <= a:
        a += arr[i][1]
        solved += 1
    else:
        break
print(solved)
