from collections import deque

def solution(priorities, location):
    # 프로세스의 위치를 담아주고
    pro = [i for i in range(len(priorities))]
    # 프로세스의 번호마다 실행한 순서를 기록할 딕셔너리
    p_dic = {i:-1 for i in range(len(priorities))}
    # 이 두가지를 모두 deque의 queue로 지정한다.
    queue = deque(priorities)
    p_queue = deque(pro)
    order = 1
    # queue가 모두 실행할 때 까지 반복하며
    while queue:
        # queue의 max값이 queue의 첫번째면 
        if max(queue) == queue[0]:
            # queue를 삭재하고
            queue.popleft()
            # 해당 queue의 실행 순서를 넣고
            p_dic[p_queue.popleft()] = order
            # 순서를 + 1
            order += 1
        # max값이 아니라면
        else:
            # queue값과 프로세스의 위치를 popleft하고
            pri = queue.popleft()
            num = p_queue.popleft()
            # 다시 맨 뒤에 삽입한다.
            queue.append(pri)
            p_queue.append(num)
            
            
    # 마지막으로 알고자 하는 프로세스의 실행순서를 반환.
    return p_dic[location]