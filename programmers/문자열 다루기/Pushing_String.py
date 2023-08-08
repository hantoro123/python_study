def solution(A, B):
    answer = 0
    # 각 문자열을 list형으로 변환한다.
    A_string = list(A)
    B_string = list(B)
    # 문자열의 길이 만큼 반복한며
    for i in range(len(A)):
        # 만약에 두 문자열 리스트가 같다면 answer를 return
        if A_string == B_string:
            return answer
        # 다르다면 answer를 하나 올리고
        answer += 1
        # A의 마지막 문자를 pop하고
        temp = A_string.pop()
        # A의 가장 앞에 넣는다.
        A_string.insert(0,temp)
    
    # 한바뀌를 다 돌았는데 다르다면 answer를 -1로 하고 return
    answer = -1
    return answer