import sys

# n의 수를 입력받고
n = int(sys.stdin.readline().rstrip())
# 1, n까지 들어갈 stack과 push, pop할때 +, - 가 들어갈 리스트
stack = []
can = []
# 수열이 들어간 리스트를 reverse 시켜준다.
sequence = [int(sys.stdin.readline()) for _ in range(n)]
sequence.reverse()

for i in range(1,n+1):
    # 일단 1부터 숫자를 stack에 넣고 넣었으니 +를 can에 넣는다.
    stack.append(i)
    can.append('+')
    # stack이 존재하고 stack과 sequence의 끝이 같으면
    if len(stack) != None and stack[-1] == sequence[-1]:
       while len(stack) != 0 and stack[-1] == sequence[-1]:
           # 서로 끝을 pop하고 -를 can에 넣고 반복
           stack.pop()
           sequence.pop()
           can.append('-')
    
# 1,n까지 stack이 만약에 수열을 만들지 못해 남아있다면
if len(stack) != 0:
    print('NO')
else:
    # 수열을 만들었으면 can을 출력
    for i in can:
        print(i)