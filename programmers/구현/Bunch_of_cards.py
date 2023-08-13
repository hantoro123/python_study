def solution(cards1, cards2, goal):
    # 카드 1과 2의 시작 주소
    c1 = 0
    c2 = 0
    # 목표의 각 단어들을 돌묘
    for g in goal:
        while True:
            # 현재 단어가 card1의 현재 주소에 단어와 같다면
            if len(cards1) > c1 and cards1[c1] == g:
                # c1을 + 1해주고
                c1 += 1
                break
            # 현재 단어가 card2의 현재 주소에 단어와 같다면
            elif len(cards2) > c2 and cards2[c2] == g:
                # c2를 + 1해준다.
                c2 += 1
                break
            # 만약에 두 카드 모두 다르다면 No를 반환
            else:
                return "No"
        
    # 모든 카드로 goal을 만들 수 있으면 Yes 반환
    return "Yes"