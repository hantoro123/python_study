from collections import deque
import sys

N,M,R = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)

check = [True for _ in range(N+1)]
visited = [0 for _ in range(N)]

def bfs(E,R):
    c = 1
    q = deque()
    q.append(R)
    while q:
        u = q.popleft()
        if check[u]:
            check[u] = False
            visited[u-1] = c
            c += 1
            for v in sorted(E[u]):
                q.append(v)

    return

bfs(edges,R)
for j in visited:
    print(j)