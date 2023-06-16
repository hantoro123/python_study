from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 던전에 들어가는 모든 조합순열을 넣는다.
    permu = list(permutations(range(0,len(dungeons)),len(dungeons)))
    
    # 각 조합마다 반복하며
    for p in permu:
        prd = k
        cnt = 0
        # 반복하고
        for i in p:
            # 현재 피로도가 dongeons[i][0]보다 크면
            if prd >= dungeons[i][0]:
                # 현재피로도 에서 [i][1]을 빼준다.
                prd -= dungeons[i][1]
                # 횟수도 + 1
                cnt += 1
        # answer와 cnt중 max값을 넣어준다.
        answer = max(answer,cnt)
    
    # answer를 반환한다.
    return answer