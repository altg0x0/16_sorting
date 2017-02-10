import sys
from bisect import bisect_left
m = int(input())
segs = []
inp_raw = input()
while inp_raw != '0 0':
    inp = list(map(int, inp_raw.split()))
    segs.append([inp[0], inp[1]])
    inp_raw = input()
segs.sort()
last = 0
ind = -1
cover = []
lefts = list(map(lambda x: x[0], segs))
while last < m:
    max_ind = bisect_left(lefts, last + 1) - 1
    if ind == max_ind:
        print('No solution')
        sys.exit()
    ind = max(range(ind + 1, max_ind + 1), key=lambda x: segs[x][1])
    last = segs[ind][1]
    cover.append(segs[ind])
print(len(cover))
print(*(' '.join(map(str, x)) for x in cover), sep='\n')
