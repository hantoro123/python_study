def solution(my_string, num1, num2):
    # 현재 문자열을 list로 하나 하나 넣어주고
    my_string = list(my_string)
    # 해당하는 index의 값을 동시에 바꿔 준다.
    my_string[num1],my_string[num2]=my_string[num2],my_string[num1]
    print(my_string)
    
    # my_string 리스트를 join해서 반환한다.
    return ''.join(my_string)