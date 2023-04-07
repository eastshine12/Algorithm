import sys

N = int(sys.stdin.readline().strip())

map_list = []
for _ in range(N):
    li = list(sys.stdin.readline().strip())
    map_list.append(li)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(graph, root):

    stack = [root]
    global visit
    visit[root[0]][root[1]] = True

    while stack:
        n = stack.pop()

        for i in range(4):
            nx = n[0] + dx[i]
            ny = n[1] + dy[i]

            # 영역을 벗어나는 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 이미 방문한 경우 무시
            if visit[nx][ny]:
                continue

            # 움직이기 전 값과 움직인 후 값이 같은 경우는 같은 영역
            if graph[n[0]][n[1]] == graph[nx][ny]:
                visit[nx][ny] = True
                stack.append([nx, ny])


# 적녹색약 아닌 사람
visit = []
for i in range(N):
    visit.append([False] * N)

cnt = 0

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            dfs(map_list, [i, j])
            cnt += 1

print(cnt)


# 적녹색약인 사람
visit = []
for i in range(N):
    visit.append([False] * N)

cnt = 0

for i in range(N):
    for j in range(N):
        if map_list[i][j] == 'G':
            map_list[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            dfs(map_list, [i, j])
            cnt += 1

print(cnt)