import sys

n = int(sys.stdin.readline())
liveCompany = set()

for i in range(n):
    name, do = sys.stdin.readline().split()
    if do == 'enter':
        liveCompany.add(name)
    else:
        liveCompany.remove(name)

currentCompany = sorted(liveCompany, reverse=True)
print('\n'.join(currentCompany))