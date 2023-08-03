def solution(brown, yellow):
    answer = []
    # 카펫의 전체 면적이고
    carpet = brown+yellow
    
    # 3*3이 최소값이므로 3부터 시작한다.
    for i in range(3,carpet+1):
        j = carpet//i
        # carpet이 i로 나누어 떨어지면 i가 x고 몫인 j가 y값이다.
        if carpet%i == 0 and (i-2)*(j-2) == yellow:
            # 그리고 i-2와 j-2를 곱한값이 yellow의 면적과 같다면
            # answer에 [i,j]를 넣고
            answer = [i,j]
    
    # 찾은 answer를 반환
    return answer