def solution(s):
    # 문자열을 담을 stack
    stack = []
    # 문자열의 길이만큼 반복하며
    for i in range(len(s)):
        # stack이 존재하면
        if stack:
            # 마지막 문자열과 같은지 비교휴
            if stack[-1] == s[i]:
                # 같으면 pop
                stack.pop()
            else:
                # 다르면 s[i]를 삽입
                stack.append(s[i])
        else:
            # stack이 비어 있다면 삽입
            stack.append(s[i])

    # stack을 다 제거 못하면 0 제거하면 1을 반환            
    if stack:
        return 0
    else:
        return 1
    