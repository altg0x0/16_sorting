name = dict()
messages = dict()
root = dict()
n = int(input())
for i in range(n):
    m = int(input())
    if not m:
        name[i] = input()
        messages[i] = 1
        root[i] = i
        input()
    else:
        m -= 1
        messages[root[m]] += 1
        root[i] = root[m]
        input()
print(name[max(messages, key=lambda x: messages[x])])
