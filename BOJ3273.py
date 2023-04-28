import sys

# 숫자를 받은 변수
n = int(sys.stdin.readline())
# 들어올 수열 리스트를 정렬해서 받아준다.
sequence = sorted(list(map(int, sys.stdin.readline().split())))
# 목표로 하는 합의 값
x = int(sys.stdin.readline())
# 몇개인지 확인하는 변수
cnt = 0
# 수열의 처음과 끝
start,end =0, n-1


while True:
    # start와 end가 같으면 반복을 멈추고 
    if start == end:
        break

    # 각 인덱스의 합이 작으면 start + 1
    if sequence[start]+sequence[end] < x:
        start += 1
    # 같으면 카운트 + 1, end - 1
    elif sequence[start]+sequence[end] == x:
        cnt += 1
        end -= 1
    # 합이 크면 end - 1
    else:
        end -= 1

# 최종합 출력
print(cnt)