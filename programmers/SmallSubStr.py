def solution(t, p):
    answer = 0
    # p의 자릿 수
    plen = len(p)

    # t의 길이 만큼 반복하며
    for i in range(len(t)):
        #i+plen이 t의 길이보다 길어지면 break
        if i+plen > len(t):
            break
    
        # p보다 부분 문자열이 작거나 같으면
        if int(p) >= int(t[i:i+plen]):
            # answer += 1
            answer += 1
    
    # answer를 반환
    return answer