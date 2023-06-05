import heapq
# heapq를 import

def solution(scoville, K):
    answer = 0
    # scoville을 heap으로 변환
    heapq.heapify(scoville)
    
    # scoville[0]이 K보다 작으면 반복
    while scoville[0] < K:
        # scobille이 1개만 있으면
        if len(scoville) == 1:
            # K보다 크면 바로 반환
            if scoville[0] > K:
                return answer
            # K보다 작거나 같으면 -1 반환
            return -1
        
        # scoville의 heap을 두번 재거하고
        sco_min1 = heapq.heappop(scoville)
        sco_min2 = heapq.heappop(scoville)
        # scoville에 min1과 min2*2를 더한 값을 push한다.
        heapq.heappush(scoville, sco_min1+sco_min2*2)
        # answer += 1한다.
        answer += 1
    
    # answer를 반환한다.
    return answer