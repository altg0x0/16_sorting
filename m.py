s = int(input()) - 3
n = int(input())
arr = sorted(list(map(int, input().split())))
gen = (x for x in arr if x >= s + 3)
c = 0
for i in gen:
    c += 1
    s = i
print(c)
