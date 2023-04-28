import sys

K = int(sys.stdin.readline())
accountBook = []

for i in range(K):
    money = int(sys.stdin.readline())
    if money == 0:
        accountBook.pop()
    else:
        accountBook.append(money)

print(sum(accountBook))