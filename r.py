n = int(input())
ar = list(map(int, input().split()))
indices = sorted(enumerate(ar), key=lambda x: x[1], reverse=True)
print(sum((i + 1) * indices[i][1] for i in range(n)))
print(*(x + 1 for x, y in indices))