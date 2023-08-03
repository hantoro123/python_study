import math

def solution(n,a,b):
    answer = 0
    # a,b의 부모 노드가 같아질때까지 반복
    while a != b:
        # 각각을 2로 나누고 올림을 해준다.
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        # 부모를 찾기위한 연산을 할때마다 +1을 해준다.
        answer += 1

    # 부모가 같아지는 횟수를 출력
    return answer