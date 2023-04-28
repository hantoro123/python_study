import sys

n = int(sys.stdin.readline())
# 집합 구조를 이용
liveCompany = set()

# 변수를 나눠 받아 liveCompany에 넣는다.
for i in range(n):
    name, do = sys.stdin.readline().split()
    if do == 'enter':
        liveCompany.add(name)
    else:
        liveCompany.remove(name)

# 역으로 정렬하고 출혁한다.
currentCompany = sorted(liveCompany, reverse=True)
print('\n'.join(currentCompany))