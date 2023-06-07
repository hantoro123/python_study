def solution(numbers):
    # 각 숫자를 문자열로 만들어 각 문자열을 4번 복사한 값의 앞에서 부터 4개의 문자열을 가지고
    #  내림차순으로 정렬한다.
    num = sorted(list(map(str,numbers)), reverse=True, key=lambda x:(x*4)[:4])
    # 정렬된 문자를 모아 int형으로 바꾸고
    answer = int(''.join(num))
    # 문자열로 다시 바꿔 반환
    return str(answer)