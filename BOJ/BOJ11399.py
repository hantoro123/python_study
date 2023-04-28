import sys

# 사람의 수와 사람들이 인출하는데 걸리는 시간을 받고 정렬한다.
N = int(sys.stdin.readline())
persons = sorted(list(map(int, sys.stdin.readline().split())))
total_time = 0

# 가장 첫번째 사람은 N번 더해질거고 그다음 사람은 N-1번 더해질 거기 때문에
# i 사람은 N-i 번 더해진다. 이를 모두 더하면 total_time
for i in range(N):
    total_time += persons[i] * (N-i)

print(total_time)