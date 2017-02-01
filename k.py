from operator import itemgetter
from itertools import groupby
n = int(input())  # I would use set(arr) IRL
ar1 = list(map(int, input().split()))
m = int(input())
ar2 = list(map(int, input().split()))
ar1.sort()
ar2.sort()
print('YES' if list(map(itemgetter(0), groupby(ar1))) == list(map(itemgetter(0), groupby(ar2))) else 'NO')
