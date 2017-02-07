import sys, functools
inp = sys.stdin.read()[:-1]
arr = sorted(inp.split('\n'), key=lambda x: (x.ljust(100, x[-1]), -len(x)), reverse=True)
print(''.join(arr))
