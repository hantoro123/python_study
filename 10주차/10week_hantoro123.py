## 숫자 게임 2303

import sys

def num_game(P):
    m=0; n=0           # 카드 세수합의 일의자리 max값과 현재 순서에서 합의 일의자리
    for n1 in range(0,3):
        for n2 in range(n1+1,4):
            for n3 in range(n2+1,5):
                n = (p[n1]+p[n2]+p[n3])%10   # p배열에 3수의 합 의 10으로 나눈 나머지
                if m <= n:          # 비교후 크면 넣기
                    m = n
    return m

N = int(sys.stdin.readline())           # 사람수 받기
p = []; num=0; m_num=0                  # p배열, 카드번호의 일의자리, 가장큰수
for i in range(0,N):
    p = list(map(int,sys.stdin.readline().split()))  # 순서 사람의 카드들
    num = num_game(p)                   # game에 배열 넣기
    if m_num <= num:                    # 현재 순서의 카드번호와 현재 가장 큰값과 비교
        m_num = num                     # 더 크면 값 넣어주기
        order = i + 1                   # 그때 순서 알아두기

print(order)
 
## 종이 자르기 2628

column, row = map(int, input().split())  # 초기 열과 행 받기
r = [0]; c = [0]                         # 자를 열과 행 배열 만들어 놓기
n = int(input())                         # 몇번 자를지

for i in range(0, n):
    a,b = map(int, input().split())      # a 행인지 열인지, b 몇번째 점선 자를지
    if a == 0:                           # 행자르기
        r.append(b)
    else:                                # 열자르기
        c.append(b)
r.sort(); c.sort()                       # 자를 열과행 각각 sort
r.append(row); c.append(column)          # 0~자를행,열까지 들어가있으니 마지막 초기 마지막 행열 git
r_max=[]; c_max=[]                       # 자른 행열의 각 길이의 배열
for i in range(0, len(r)-1):
    r_max.append(r[i+1]-r[i])
for j in range(0,len(c)-1):
    c_max.append(c[j+1]-c[j])

print(max(r_max)*max(c_max))             # 각 행,열 max값 곱하면 가장 넓은 종이 나옴
 
## 절사평균 6986
import sys

def col_a(s,N,K):                           # 보정평균
    sum_s = (s[K]*K)+sum(s)+(s[-K-1]*K)     # 합은 0이 아닌 K번째가 K개 더생김 +나머지합 + 0이아님 -K-1번째가 K개 더생김
    average = sum_s/N+(1e-8)                # 마찬가지로 부동소수 오차때문에 작은값 더해주기
    print(f"{average :.2f}")

def cut_a(s,N,K):                           # 절사평균
    for i in range(K):                      # 0 ~ K-1 까지 0으로 바꿔주기
        s[i] = 0
    for j in range(-1,-K-1,-1):             # -1 ~ -K 까지 0으로 바꿔주기
        s[j] = 0
    average = sum(s)/(N-2*K)+(1e-8)         # 평균 = 더한거/(전체-2K) 부동소수 오류 때문에 매우 작은값 더해줘야함
    print(f"{average :.2f}")
    return col_a(s,N,K)                     # 앞뒤가 0인 s배열가지고 보정평균으로 넘어가기

N, K = map(int, sys.stdin.readline().split()) # N, K받기
score = [0]*N                                 # 점수 배열 미리 N개 생성

for i in range(N):
    score[i] = float(sys.stdin.readline())    # 소수로 각각 입력받기

s = sorted(score)                             # sorted함수 이용 퀵정렬이랑 비슷
cut_a(s,N,K)