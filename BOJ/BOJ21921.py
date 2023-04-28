import sys

# 입력받을 변수
N, X = map(int, sys.stdin.readline().split())
# 방문자 수
visit = list(map(int, sys.stdin.readline().split()))

# 첫날부터 X일까지 방문자수를 maxTotal로 지정하고 그 수를 cnt에 저장
totalSum = sum(visit[:X])
cnt = [totalSum]
maxTotal = totalSum

for i in range(X,N):
    # 다음 방문자의 총합은 첫날을 빼고 마지막 다음날을 추가
    totalSum += visit[i] - visit[i-X]
    cnt.append(totalSum)
    maxTotal = max(maxTotal, totalSum)

# 총 방문자가 0이면 SAD
if maxTotal == 0:
    print("SAD")
else:
    # 방문자 수가 있다면 그 수와 몇번 그랬는지 출력
    print(maxTotal)    
    print(cnt.count(maxTotal))