import sys
from collections import deque

max = 100000
N, K = map(int, sys.stdin.readline().split())
arr = [0] * (max + 1)


def bfs():
    queue = deque([N])
    while queue:
        q = queue.popleft()
        if q == K:
            return arr[q]
        for i in (q-1, q+1, q*2):
            if 0 <= i <= max and not arr[i]:
                arr[i] = arr[q] + 1
                queue.append(i)


print(bfs())