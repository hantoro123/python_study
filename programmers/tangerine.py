def solution(k, tangerine):
    # 답을 0으로 초기화
    answer = 0
    # 귤이 몇개 있는지 담을 딕셔너리
    tang_cnt = dict()
    for i in tangerine:
        # 귤이 1개 이상 있다면
        if tang_cnt.get(i):
            # +1개를 해주고
            tang_cnt[i] += 1
        else:
            # 아직 없었다면 1개로 한다.
            tang_cnt[i] = 1
    
    # 딕셔너리의 아이템으로 정렬해주고
    tang = dict(sorted(tang_cnt.items(), key=lambda x:x[1], reverse=True))
    for t in tang:
        # k에서 큰 수만큼 빼주고 answer에 +1
        answer += 1
        k -= tang[t]
        # k가 다 줄어들면 break
        if k <= 0:
            break
    # 답을 반환
    return answer