
def solution(topping):
    answer = 0
    # topping 갯수
    tcnt = len(topping)
    # 형이 진행하면서 몇개씩 가지고 있는지와
    big = [0 for _ in range(tcnt)]
    # 형이 어떤걸 가지고 있는지 집합으로 중복 없이 체크
    b_list = set()
    # 동생이 진행하면서 몇개씩 가지고 있는지와
    little = [0 for _ in range(tcnt)]
    # 동생이 어떤걸 가지고 있는지
    l_list = set()
    # topping의 갯수만큼 진행하면서
    for i in range(tcnt):
        # 형을 왼쪽 동생을 오른쪽에서 시작해서 토핑을 담고
        b_list.add(topping[i])
        l_list.add(topping[tcnt-i-1])
        # 현재 형, 동생이 가진 토핑의 가지수를 넣는다.
        big[i] = len(b_list)
        little[tcnt-1-i] = len(l_list)
    
    # topping 갯수만큼 반복하며
    for j in range(tcnt):
        # j+1이 tcnt보다 커지면 멈추고
        if j+1 >= tcnt:
            break
            
        # 형과 동생이 가진 topping의 수가 같으면 answer의 수를 +1 해준다.
        if big[j] == little[j+1]:
            answer += 1
    # 최종적으로 answer를 반환한다.
    return answer