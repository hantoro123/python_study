import sys

N, M = map(int, sys.stdin.readline().split())
Dict = {}
Dictnum = {}

for i in range(1,N+1):
    poketmon = sys.stdin.readline().rstrip()
    Dict[poketmon] = i
    Dictnum[i] = poketmon

for j in range(M):
    problem = sys.stdin.readline().rstrip()
    try:
        problem = int(problem)
        print(Dictnum[problem])
    except ValueError:
        print(Dict[problem])