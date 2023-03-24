import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

map_list = []

for i in range(N):
    li = list(map(int, sys.stdin.readline().split(' ')))
    map_list.append(li)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])

for i in range(N):
    for j in range(M):
        if map_list[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if map_list[nx][ny] == 0:
                map_list[nx][ny] = map_list[x][y] + 1
                queue.append([nx, ny])


bfs()


def solution():
    result = 0

    for i in map_list:
        for j in i:
            if j == 0:
                return -1
        result = max(result, max(i))

    return result - 1


print(solution())
