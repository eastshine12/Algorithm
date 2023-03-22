import sys
from collections import deque

com = int(sys.stdin.readline())
line = int(sys.stdin.readline())

graph_list = {key: [] for key in range(1, com + 1)}

for i in range(line):
    a, b = map(int, sys.stdin.readline().split())
    graph_list[a].append(b)
    graph_list[b].append(a)


def bfs(graph, root):
    visit = []
    queue = deque([root])
    cnt = 0
    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            queue.extend(graph[n])
            if n != root:
                cnt += 1

    return cnt


print(bfs(graph_list, 1))
