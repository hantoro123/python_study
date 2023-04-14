import sys

# 채팅 기록 수 와 곰곰티콘 사용 횟수
N = int(sys.stdin.readline())
cnt = 0

for i in range(N):
    # 오른쪽 공백없이 입력받고
    user = sys.stdin.readline().rstrip()
    # 입력값이 ENTER라면 member 딕셔너리 생성
    if user != "ENTER":
        # ENTER가 아니면 user가 처음 들어온 user인지 확인하고
        if user in member:
            continue
        else:
            # 처음 들어왔으면 값을 True cnt는 + 1
            member[user] = True
            cnt += 1
    else:
        member = {}

print(cnt)