import sys

T = int(sys.stdin.readline())

def stack(ps):
    top = -1
    st = []
    for i in ps:
        if i == '(':
            st.append(i)
            top += 1
        else:
            if top != -1 and st[top] == '(':
                st.pop()
                top -= 1
            else:
                return False
    if top == -1:      
        return True
    else:
        return False
                

for i in range(T):
    PS = list(sys.stdin.readline().rstrip())
    if stack(PS):
        print("YES")
    else:
        print("NO")