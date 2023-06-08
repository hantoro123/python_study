def solution(citations):
    # 인용된 논문의수
    n = len(citations)
    answer = n
    # 논문의 수를 정렬하고
    citations = sorted(citations)
    
    # 논문의 수가 1이면 1을 바로 반환
    if n == 1:
        return 1
    
    # 논문 수만큼 반복하고
    for c in range(n):
        print(citations[c],answer)
        # citaions[c]가 answer보다 크거나 같으면
        if citations[c] >= answer:
            # answer를 바로 반환
            return answer
        else: # citaions[c]가 answer보다 작으면
            # answer값을 1씩 줄인다.
            answer -= 1
    
    # 인용된 논문이 모두 0이면 0을 반환
    return 0