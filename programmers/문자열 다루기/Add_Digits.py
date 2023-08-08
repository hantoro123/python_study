def solution(n):
    answer = 0
    # n을 문자열로 변환하고
    n_string = str(n)
    for num in n_string:
        # answer에 각 자릿수의 숫자를 더해준다.
        answer += int(num)
    
    # 총합 answer를 반환한다.
    return answer