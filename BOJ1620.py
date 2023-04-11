import sys

N, M = map(int, sys.stdin.readline().split())
# key 값이 포켓몬 이름으로 들어올 딕셔너리와 key 값이 번호를 들어올 딕셔너리 두개를 만든다.
Dict = {}
Dictnum = {}

# 1번 부터 N번까지 돌며 각 딕셔너리에 넣어준다.
for i in range(1,N+1):
    poketmon = sys.stdin.readline().rstrip()
    Dict[poketmon] = i
    Dictnum[i] = poketmon

# 문제를 입력하고
for j in range(M):
    problem = sys.stdin.readline().rstrip()
    # 문제가 int로 바꿀 수 있으면 바꾸고 번호 딕셔너리에서
    try:
        problem = int(problem)
        print(Dictnum[problem])
    # 못 바꾸면 포켓폰 이름 딕셔너리에서 찾아 출력해준다.
    except ValueError:
        print(Dict[problem])