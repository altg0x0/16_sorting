from bisect import bisect as bis


def shift(a, beg, end):
    p = end
    while p > beg:
        a[p] = a[p - 1]
        p -= 1


n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    el = arr[i]
    ins = bis(arr[:i], el)
    if ins == i:
        continue
    shift(arr, ins, i)
    arr[ins] = el
    print(*arr)
