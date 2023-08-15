def solution(my_str, n):
    answer = []
    # 시작 주소를 시작으로
    start = 0
    # 시작주소 + n 이 my_str의 길이보다 길면 멈춘다.
    while start + n < len(my_str):
        # start:start+n으로 슬라이싱 후 answer에 넣어주고
        answer.append(my_str[start:start+n])
        # start는 + n 해준다.
        start += n
    
    # 그리고 마지막으로 안들어간 부분까지 넣어준다.
    answer.append(my_str[start:])
    # answer를 반환해준다.
    return answer