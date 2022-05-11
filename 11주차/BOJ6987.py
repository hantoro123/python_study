## BOJ 6987 월드컵

import sys
from itertools import combinations # combinations(range(범위숫자), 몇개로 조합할지)

def w_cup(round):
    global r                      # r을 글로벌 변수로 받고
    if round == len(game):        # round가 game의 수만큼 진했했다면
        r = 1                     # r = 1
        for i in team:
            if i.count(0) != 3:   # 팀 목록마다 승,무,패 가 모두 0이 아니면
                r = 0             # r = 0
                break
        return                    # 조건이 만족후 return 재귀후 남아있는 다른 함수들 마져 실향
 
    t1,t2 = game[round]                          # 라운드 마다 경기하는팀 t1, t2
    for x,y in ((0,2),(1,1),(2,0)):              # 0이 승 1이 무승부 2가 패
        if team[t1][x] > 0 and team[t2][y] > 0:  # 두경우가 둘가 0보다 크면
            team[t1][x] -= 1
            team[t2][y] -= 1                     # 라운드 진행시 각각을 -1
            w_cup(round + 1)                     # 재귀로 round를 +1 해서한다.
            team[t1][x] += 1                     # 계속 재귀를 하다가 중지되거나 모든 조건이 끝나면
            team[t2][y] += 1                     # 19 다음줄 부터 스택처럼 실행

game=list(combinations(range(6),2)) # (0,1),(0,2),(0,3), ~~~ (3,4)(3,5)(4,5) 총 15개
result = []             # 총 결과
for _ in range(4):      # 네번 반복
    score = list(map(int,sys.stdin.readline().split()))  # 조별 점수 받기
    team = [score[i:i+3] for i in range(0,16,3)]         # 각 조에 승,무,패, 점수 넣기
    r = 0                                                # r = 0 으로 초기화
    w_cup(0)                                             # round=0
    result.append(r)                                     # 최종 r 넣기

print(*result)                                           # 리스트 출력