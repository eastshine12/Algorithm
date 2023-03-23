import sys

N = int(sys.stdin.readline().strip())
map_list = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
result = 0
result_cnt = []

for i in range(N):
    map_list.append(list(map(int, sys.stdin.readline().strip())))


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if map_list[x][y] == 1:
        global cnt
        cnt += 1
        map_list[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

    return False


for i in range(N):
    for j in range(N):
        if dfs(i, j):
            result_cnt.append(cnt)
            result += 1
            cnt = 0

print(result)
result_cnt.sort()
for i in result_cnt:
    print(i)
