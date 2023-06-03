from math import ceil
def solution(progresses, speeds):
    answer = []
    # 작업의 개수 만큼 진행하며
    for i in range(len(speeds)):
        # 각 인덱스의 작업을 (100-작업량)/작업속도 하고 이값을 올림하여 나온 작업일수를 다시 넣는다.
        progresses[i] = ceil((100-progresses[i])/speeds[i])
    
    
    cnt = 1
    # 첫 작업의 작업일을 넣고
    big_day = progresses[0]
    # 1번 부터 작업의 수만큼 반복
    for j in range(1,len(progresses)):
        # 만약 big_day보다 현재 작업일이 더 크다면
        if big_day < progresses[j]:
            # answer에 지금까지 마친 작업의 양을 넣고
            answer.append(cnt)
            # big_day를 현재 작업일로 변경
            big_day = progresses[j]
            # 종료한 작업일은 1로 초기화
            cnt = 1
        else:
            # 현재 작업일이 더 작으면 종료한 작업의 수를 +1
            cnt += 1
    
    # 반복이 끝나고 cnt를 한번더 answer에 넣어주고 반환
    answer.append(cnt)
    return answer