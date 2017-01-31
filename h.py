def part(ar, beg, end):
    piv = beg
    for i in range(beg + 1, end + 1):
        if ar[i] <= ar[beg]:
            piv += 1
            ar[i], ar[piv] = ar[piv], ar[i]
    ar[piv], ar[beg] = ar[beg], ar[piv]
    return piv


def qsort(ar, beg, end):
    if beg >= end:
        return
    piv = part(ar, beg, end)
    qsort(ar, beg, piv - 1)
    qsort(ar, piv + 1, end)
    return ar

n = int(input())
arr = list(map(int, input().split()))
print(*qsort(arr, 0, n - 1) if len(arr) > 1 else arr)
# Not a copy
