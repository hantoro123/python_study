import sys

# 변수를 담아둘 변수 생성
N, M = map(int, sys.stdin.readline().split())
count = 0
# 비교할 문자열 집합 생성
stringSet = [sys.stdin.readline() for _ in range(N)]

# M개만큼 비교후 집합 안에 있으면 count를 +1
for i in range(M):
    string = sys.stdin.readline()
    if string in stringSet:
        count += 1

print(count)