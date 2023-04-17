import sys

# 플레이어수와 방의 정원을 입력
p, m = map(int, sys.stdin.readline().split())

# players는 key를 player level을 value로 하는 딕셔너리로 받고 
# rooms는 리스트로 각 방에 들어가는 player를 저장한다.
players = {}
rooms = []
# 각 player당 level을 저장한다.
for i in range(p):
    level, player = sys.stdin.readline().split()
    players[player] = int(level)

for i in players.keys():
    # 방에 들어갔느지 여부
    enter = False
    for r in range(len(rooms)):
        # 방의 정원이 넘어가면 다음 방으로
        if len(rooms[r]) == m:
            continue

        # 방에 들어갈 수 있는지 확인후 들어가면 여부를 True로
        if players[rooms[r][0]]-10 <= players[i] <= players[rooms[r][0]]+10:
            rooms[r].append(i)
            enter = True
            break

    # 못들어갔다면 새로운방에 넣는다.
    if not enter:
        rooms.append([i])

# 방 마다 돌며 start인지 waiting인지 검사후 출력
for i in range(len(rooms)):
    if len(rooms[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    # rooms에 닉네임이 있으니 정렬 후 출력
    rooms[i].sort()
    for r in rooms[i]:
        print(f'{players[r]} {r}')
