def solution(s):
    # 괄호의 )를 키로 (를 value로
    p = {")":"("}
    # 괄호를 넣을 스택
    stack = []
    # s반큼 반복하고
    for i in s:
        # )이 들어오고, stack이 존재하며 stack의 마지막이 (라면
        if p.get(i) and stack and stack[-1] == p[i]:
            # stack을 pop
            stack.pop()
        else:
            # 아니라면 stack에 push
            stack.append(i)
    
    # 만약에 stack이 남아있으면 False
    if stack:
        return False

    # stack이 비어있다면 올바를 괄호이므로 True
    return True