import itertools
delim = '**********'
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
buckets = [[] for _ in range(10)]
print("Initial array:")
print(*arr, sep=', ')
print(delim)
for i in range(1, len(str(arr[0])) + 1): # log10 would be better
    for j in arr:
        buckets[j % 10 ** i // (10 ** (i - 1))].append(j)
    print('Phase ' + str(i))
    for t in range(10):
        print('Bucket ' + str(t) + ': ', end='')
        print(', '.join(map(str, buckets[t])) if buckets[t] else 'empty')
        print(delim)
    arr = list(itertools.chain(*buckets))
    buckets = [[] for _ in range(10)]
print(delim)
print("Sorted array:")
print(*arr, sep=', ')
