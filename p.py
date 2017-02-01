from collections import Counter
n = int(input())
maxims = list(map(int, input().split()))
k = int(input())
presses = list(map(int, input().split()))
c = Counter(presses)
for i in enumerate(maxims):
    print('yes' if c[i[0] + 1] > i[1] else 'no')
