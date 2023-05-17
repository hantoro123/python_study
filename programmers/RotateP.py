def solution(s):
    # 괄호의 오른쪽을 key로 왼쪽을 value
    prt = {'}':'{',']':'[',')':'('}
    # s의 길이와 올바른 괄호인지 횟수를 저장
    s_len = len(s)
    cnt = 0
    for i in range(s_len):
        # s의 길이만큼 반복하고
        # s를 하나씩 읽으며 저장할 stack
        stack = []
        for p in s:
            # 만약 stack이 비어있거나, Key값이 없다면 stack에 추가
            if not stack or prt.get(p) == None:
                stack.append(p)
            # stack의 마지막과 P에 해당하는 value값이 같으면 stack을 pop
            elif stack[-1] == prt[p]:
                stack.pop()
        
        # stack이 비어있으면
        if not stack:
            # cnt를 증가
            cnt += 1
        # s를 0번째를 맨뒤로 보낸다.
        s = s[1:]+s[0]

    # cnt를 반환
    return cnt