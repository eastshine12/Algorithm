import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

map_list = []
for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    map_list.append(arr)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
wall = []

# 바이러스 좌표, 빈 칸 좌표 담기
for i in range(N):
    for j in range(M):
        if map_list[i][j] == 0:
            wall.append([i, j])
        if map_list[i][j] == 2:
            virus.append([i, j])

three_walls = [c for c in combinations(wall, 3)]


def dfs(graph, root):

    stack = root

    while stack:
        n = stack.pop()

        for i in range(4):
            nx = n[0] + dx[i]
            ny = n[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 2:
                continue

            # 벽 or 바이러스 무시
            if graph[nx][ny] == 1 or graph[nx][ny] == 2:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                stack.append([nx, ny])

    cnt = 0

    for i in graph:
        for j in i:
            if j == 0:
                cnt += 1

    return cnt


result = 0

for a, b, c in three_walls:
    # 깊은 복사 (slicing 이 deepcopy 보다 빠름)
    map_list_cp = [arr[:] for arr in map_list]
    map_list_cp[a[0]][a[1]] = 1
    map_list_cp[b[0]][b[1]] = 1
    map_list_cp[c[0]][c[1]] = 1

    virus_cp = virus[:]
    total = dfs(map_list_cp, virus_cp)

    result = max(total, result)

print(result)
