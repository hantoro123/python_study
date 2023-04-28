import sys

n = int(sys.stdin.readline())

strings = list(set([sys.stdin.readline().rstrip() for _ in range(n)]))
strings.sort(key=lambda x:(len(x),x))
print(strings)
for i in strings:
    print(i)