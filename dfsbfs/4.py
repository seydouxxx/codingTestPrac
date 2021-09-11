# 152p

from collections import deque

def solution(n, m, a):
    queue = deque()
    queue.append((0, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if a[nx][ny] == 0:
                continue
            if a[nx][ny] == 1:
                a[nx][ny] = a[x][y]+1
                queue.append((nx, ny))
    return a[n-1][m-1]
    
    
    return
# 110
# 010
# 011
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input())))
print(solution(n, m, a))