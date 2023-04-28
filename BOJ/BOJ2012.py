import sys

N = int(sys.stdin.readline())
students = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])
total = 0

for i in range(1,N+1):
    total += abs(i-students[i-1])
    
print(total)