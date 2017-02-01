n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (-x[1], x[0]))
print(*(" ".join(map(str, x)) for x in arr), sep='\n')
