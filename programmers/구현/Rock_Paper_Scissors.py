def solution(rsp):
    answer = ''
    # 가위가 2 바위가 0 보는 5 각각을 이기는 값을 value로 둔다.
    hand = {'2':'0','0':'5','5':'2'}
    # 가위바위보를 하며
    for i in rsp:
        # 이기는 문자를 answer에 더하고
        answer += hand[i]
    # answer를 반환한다.
    return answer