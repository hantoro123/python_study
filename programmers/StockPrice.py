def solution(prices):
    # 각 prices마다 언제까지 가격이 떨어지지 않는지 리스트
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)-1):
        # 각 인덱스의 price가있고
        price = prices[i]
        # 몇초에 가격이 떨어졌는지 flag
        flag = True
        for j in range(i+1,len(prices)):
            # 만약에 가격이 이후 j번째에서 가격이 떨어졌다면
            if price > prices[j]:
                # 해당 price 위치에 j-i초 만큼 유지했다는 것을 넣고
                answer[i] = j-i
                # flag를 False로
                flag = False
                # 그리고 멈춘다.
                break
        # 만약에 끝까지 떨어지지 않았다면
        if flag:
            # j-i만큼 유지했다고 넣는다.
            answer[i] = j-i
    
    # answer를 반환
    return answer