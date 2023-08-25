def solution(participant, completion):
    answer = ''
    # 모든선수가 완주를 했는지 담을 딕셔너리
    goal = {}
    # 완주한 선수 리스트를 반복하며
    for c in completion:
        # 만약에 같은이름의 완주한 선수가 이미 있다면
        if goal.get(c):
            # 동명 이인 이므로 + 1명
            goal[c] += 1
        # 해당 선수 이름으로 처음 완주했으면
        else:
            # 완주 했음을 1로 표시
            goal[c] = 1
    
    # 모든 선수 목록을 반복하며
    for p in participant:
        # 만약에 완주 목록에 존재하면서
        if goal.get(p):
            # 0이하의 숫자면
            if goal[p] <= 0:
                # 이때 사람이 완주하지 못한것
                answer = p
                # 바로 멈춘다.
                break
            # 만약 1이상이면 
            else:
                # -1을 해준다.
                goal[p] -= 1
        # 만약 완주 목록에 존재하지 않으면
        else:
            # 이 사람이 완주하지 못한것
            answer = p
            # 바로 멈춘다.
            break
            
    # 완주하지 못한 사람을 바로 반환
    return answer