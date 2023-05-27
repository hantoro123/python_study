from collections import deque

def solution(maps):
    # 정답을 담을 리스트
    answer = []
    # maps의 x,y의 길이
    x_len, y_len = len(maps),len(maps[0])
    # maps의 방문 여부를 체크할 배열
    visited = [[True for _ in range(y_len)] for _ in range(x_len)]
    # 현재 위치에서 위 아래 옆을 체크, 각 무인도의 크기를 넣을 s
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]; s= 0
    def bfs(x,y,s):
        # x,y 를 deque에 넣고
        queue = deque([x,y])
        # 현재 위치를 방문했고
        visited[x][y] = False
        # 크기에 더해준다.
        s = int(maps[x][y])
        # queue가 존재할때까지
        while queue:
            # queue의 앞을 pop해서 x에 넣고
            x = queue.popleft()
            # queue의 앞을 pop해서 y에 넣는다.
            y = queue.popleft()
            # 혹시 x나 y가 범위를 벗어나면 break
            if x >= x_len and y >= y_len:
                break
            # 4방향으로 체크하기 위해서 반복
            for i in range(4):
                nx = x+dxy[i][0]
                ny = y+dxy[i][1]
                # nx,ny가 범위 안이라면
                if 0 <= nx < x_len and 0 <= ny < y_len:
                    # 그 부분이 숫자이고, 방문 가능하다면
                    if maps[nx][ny].isnumeric() and visited[nx][ny]:
                        # queue에 각각을 넣고
                        queue.append(nx); queue.append(ny)
                        # s에 크길를 더하고
                        s += int(maps[nx][ny])
                        # 방문한걸로 체크
                        visited[nx][ny] = False
                        
        return s
    
    # 각 index만큼 돌고
    for i in range(x_len):
        for j in range(y_len):
            # maps의 현재 위치가 숫자고 방문 가능하면
            if maps[i][j].isnumeric() and visited[i][j]:
                # bfs로 들어가서 무인도의 크기를 가져옴
                sub_sum = bfs(i,j,0)
                # answer에 넣어주고
                answer.append(sub_sum)
    
    # answer의 합이 0이면 무인도가 없으므로
    if sum(answer) == 0:
        # answer를 -1
        answer = [-1]
        
    # answer를 마지막으로 정렬해서 반환
    return sorted(answer)