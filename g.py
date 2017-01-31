def merge(x, y):
    res = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            res.append(y[j])
            j += 1
        else:
            res.append(x[i])
            i += 1
    res += x[i:]
    res += y[j:]
    return res


def msort(x):
    result = []
    if len(x) <= 1:
        return x
    mid = len(x) // 2
    y = msort(x[:mid])
    z = msort(x[mid:])
    return merge(y, z)


n = int(input())
arr = list(map(int, input().split()))
print(*msort(arr))
