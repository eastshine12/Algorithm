import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
cnt = 0
map_list = {i: [] for i in range(1, N + 1)}

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    map_list[a].append(b)
    map_list[b].append(a)

visit = [False] * (N+1)


def bfs(graph, root):
    if not visit[root]:
        queue = deque([root])
        while queue:
            n = queue.popleft()
            if not visit[n]:
                visit[n] = True
                queue.extend(graph[n])
        global cnt
        cnt += 1


for i in range(1, N+1):
    bfs(map_list, i)


print(cnt)
