import sys

def push(number,top):
    stack.append(number)
    top += 1
    return top

def popStack(top):
    if top == -1:
        print(-1)
        return top
    print(stack[top])
    stack.pop()
    top -= 1
    return top

def size(top):
    print(top + 1)

def empty(top):
    if top == -1:
        print(1)
    else:
        print(0)

def topNum(top):
    if top == -1:
        print(-1)
        return
    print(stack[top])

N = int(sys.stdin.readline())
stack = []
global top
top = -1

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        top = push(command[1],top)
    elif command[0] == "pop":
        top = popStack(top)
    elif command[0] == "size":
        size(top)
    elif command[0] == "empty":
        empty(top)
    elif command[0] == "top":
        topNum(top)


