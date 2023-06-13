from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 트럭과 다리길이만큼 queue를 생성하고
    truck = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    # 다리에 올라간 무게를 체크할 변수
    w = 0
    while bridge:
        answer += 1
        # bridge의 queue를 popleft하고
        b = bridge.popleft()
        # 그값을 무게에서 빼준다.
        w -= b 
        # 만약에 대기중인 트럭이 있다면
        if truck:
            # 현재 다리에 올라간 무게와 다음으로 나갈 트럭의 무게가 버틸 수 있는 무게보다 가볍거나 같으면
            if w + truck[0] <= weight:
                # truck의 popleft하고
                t = truck.popleft()
                # 그값을 bridge에 append하고 무게를 더해준다.
                bridge.append(t)
                w += t
            else:
                # 만약 못올라 간다면 0을 bridge에 올린다.
                bridge.append(0)
                
    # 총 걸린 시간 answer를 반환 한다.
    return answer