def solution(my_string):
    answer = 0
    # 더할 자연수는 최초에 0만 가지고 있고
    num = '0'
    # my_string의 원소를 반복하며
    for s in my_string:
        # 한 문자가 숫자라면
        if s.isnumeric():
            # num에 s를 더하고
            num += s
        else:
            # 숫자가 없다면 num문자를 int형으로 변환해 더한다.
            answer += int(num)
            # num은 다시 0으로 초기화
            num = '0'
    # 마지막으로 더해지지 않은 num을 더해주고
    answer += int(num)
    
    # 최종 답을 반환
    return answer