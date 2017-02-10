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
cover = []
lefts = list(map(lambda x: x[0], segs))
lmi = -1
while last == -1 or last < m:
    max_ind = bisect_left(lefts, last + 1) - 1
    if lmi == max_ind or segs[max_ind][0] > last + 1 or segs[max_ind][0] == segs[max_ind][1]:
        print('No solution')
        sys.exit()
    last = segs[max_ind][1]
    lmi = max_ind
    cover.append(segs[max_ind])
print(len(cover))
print(*(' '.join(map(str, x)) for x in cover), sep='\n')
