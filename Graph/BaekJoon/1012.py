import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline().strip())


def solution():
    M, N, K = map(int, sys.stdin.readline().split())

    map_list = [[0]*N for _ in range(M)]

    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        map_list[a][b] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0

    def dfs(x, y):
        if x < 0 or x >= M or y < 0 or y >= N:
            return False

        if map_list[x][y] == 1:
            map_list[x][y] = 0
            for i in range(4):
                dfs(x+dx[i], y+dy[i])
            return True

        return False

    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                result += 1

    print(result)


for _ in range(T):
    solution()
