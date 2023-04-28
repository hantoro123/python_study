import sys

# 각 변수들을 대입하고, 상근이가 가진 카드와 맞출 카드를 리스트에 입력
N = int(sys.stdin.readline())
sangggeun = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
# 맞출 카드를 딕셔너리의 key값으로 해서 0으로 초기화
answer = {key : 0 for key in cards}

# 상근이가 가진 카드가 맞출 카드에 있으면 값을 +1
for i in sangggeun:
    if i in answer:
        answer[i] += 1

# 각 값을 출력
for card in cards:
    print(answer[card], end=' ')