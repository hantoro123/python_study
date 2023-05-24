import sys

sys.setrecursionlimit(10**9)

N,M,R = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)

check = [True for _ in range(N+1)]
visited = [0 for _ in range(N)]

def dfs(E,R):
    global index
    if check[R]:
        visited[R-1] = index
        index += 1
        check[R] = False
        for v in sorted(E[R],reverse=True):
            if check[v]:
                dfs(E,v)

    return

index = 1
dfs(edges,R)
for j in visited:
    print(j)
