import sys
from collections import deque
# deque를 import 한다.

N = int(sys.stdin.readline())
q = []
queue = deque(q)
# 명령의 수와 정수를 담을 queue를 생성


# 명령의 수 만큼 반복
for _ in range(N):
    # command를 list로 입력 받는다.
    command = list(sys.stdin.readline().split())
    # 0번이 push이면 
    if command[0] == 'push':
        # queue에 숫자를 push한다.
        queue.append(command[1])
    # 0번이 pop이면
    elif command[0] == 'pop':
        # queue에 원소가 존재하면
        if len(queue) >= 1:
            # pop해주고 pop한 숫자를 print한다.
            num = queue.popleft()
            print(num)
        else:
            # 원소가 없으면 -1을 출력
            print(-1)
    # 0번이 size면
    elif command[0] == 'size':
        # queue의 길이를 출력
        print(len(queue))
    # 0번이 empty면
    elif command[0] == 'empty':
        # queue의 원소가 없으면
        if len(queue) == 0:
            # 1을 출력
            print(1)
        else:
            # 원소 있으면 0 출력
            print(0)
    # 0번이 front면
    elif command[0] == 'front':
        # 원소가 없으면 -1을 출력
        if len(queue) == 0:
            print(-1)
        else:
            # 있으면 queue의 0번 원소를 출력
            print(queue[0])
    # 0번이 back면
    elif command[0] == 'back':
        # 원소가 없으면 -1을 출력
        if len(queue) == 0:
            print(-1)
        else:
            # 있으면 queue의 -1번째 원소 출력
            print(queue[-1])