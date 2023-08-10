def solution(order):
    answer = 0
    # order를 문자열로 바꾸고
    str_order = str(order)
    # 3, 6, 9의 숫자가 몇개 있는지 새고 더해준다.
    answer += str_order.count("3")
    answer += str_order.count("6")
    answer += str_order.count("9")
    
    # 총 박수를 칠 횟수를 반환한다.
    return answer