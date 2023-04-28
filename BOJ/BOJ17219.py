import sys

N, M = map(int, sys.stdin.readline().split())
password = {}

for _ in range(N):
    address, pwd = sys.stdin.readline().split()
    password[address] = pwd

for _ in range(M):
    address = sys.stdin.readline().rstrip()
    print(password[address])