import itertools
delim = '**********'
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
buckets = [[] for _ in range(10)]
print("Initial array:")
print(*arr, sep=', ')
print(delim)
for i in range(1, len(arr[0]) + 1):
    for j in arr:
        buckets[int(j[-i])].append(j)
    print('Phase ' + str(i))
    for t in range(10):
        print('Bucket ' + str(t) + ': ', end='')
        print(', '.join(buckets[t]) if buckets[t] else 'empty')
    print(delim)
    arr = list(itertools.chain(*buckets))
    buckets = [[] for _ in range(10)]
print("Sorted array:")
print(*arr, sep=', ')
