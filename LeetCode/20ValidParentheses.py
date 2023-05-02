class Solution:
    def isValid(self, s: str) -> bool:
        # valid한지 여부를 체크
        valid = True
        # s를 stack에 담아 비교
        stack = []
        # 괄호들의 오른쪽을 key로 왼쪽을 value로
        parentheses = {")":"(","}":"{","]":"["}
        for i in s:
            # 만약 괄호의 오른쪽이면 
            if i == ")" or i == "}" or i == "]":
                # stack의 마지막이 해당 괄호의 왼쪽인지 확인하고
                if stack and stack[-1] == parentheses[i]:
                    # 맞으면 pop
                    stack.pop()
                else:
                    # 아니라면 valid를 False로 하고 멈춘다.
                    valid = False
                    break
            else:
                # 괄호의 왼쪽이라면 append
                stack.append(i)

        print(stack)
        # 만약 stack에 값이 존재하면 False
        if stack:
            valid = False

        # 가능한지 여부를 return
        return valid