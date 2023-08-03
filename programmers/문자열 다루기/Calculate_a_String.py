def solution(my_string):
    # my_string을 공백을 기준으로 나누어 list로 변환한다.
    my_string = list(my_string.split())
    # 문자가 얼마나 있는지 확인하며
    str_len = len(my_string)
    # 정답에 가장 첫번째 숫자를 넣고
    answer = int(my_string[0])
    start = 1
    # 현재 위치에서 더할게 없다면 종료
    while start+2 <= str_len:
        # 연산자가 +면
        if my_string[start] == '+':
            # answer에 정수를 더해주고
            answer += int(my_string[start+1])
        else:
            # 아니면 빼준다.
            answer -= int(my_string[start+1])
        # 위치를 2칸 이동한다.
        start += 2
    
    # while이 종료되면 answer를 return한다.
    return answer
        