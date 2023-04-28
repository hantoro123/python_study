import sys

n = int(sys.stdin.readline())                                               # n*n 행렬 출력 
maps = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]     # 집위치를 2차원 리스트로 받기
count = []                                                                  # 단지가 몇개 나올건지 받을 리스트
c = 0                                                                       # 단지 하나에 집이 얼마나 나올지 확인
def dfs(x,y):                                                               # DFS 알고리즘 이용
    global c 
    if x < 0 or x > n-1 or y < 0 or y > n-1:                                # x,y좌표를 검색할때 법위를 넘어가면
        return False                                                        # False를 리턴해준다.

    if maps[x][y] == 1:                                                     # 위치가 집이있다면 (1이라면)
        maps[x][y] = 0                                                      # 그 위치를 0으로 바꿔주고
        c += 1                                                              # 지금 단지에 집의수 +1
        dfs(x + 1, y)  
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)                                                       # x,y 좌표를 각각 +-1 해보며 탐색
        return True                                                         # 전부 탐색했으면 True를 리턴
    return False                                                            # 만약 탐색한곳이 1이 아니면 False 리턴

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:                                                # DFS를 실행하고 True값이 리턴하면
            count.append(c)                                                 # count에 c를 넣어주고
            c=0                                                             # c는 0으로 초기화

count.sort()                                                                # count를 오름차순 정렬해주고
print(len(count))                                                           # count의 길이가 즉 단지 개수
for h in count:                                                             # 단지마다 집의 개수를 오름차순으로 출력
    print(h)