s1 = input()
s2 = input()
s = ''
for i in (str(x) for x in range(9, -1, -1)):
    s += i * min(s1.count(i), s2.count(i))
print(int(s) if s else -1)
