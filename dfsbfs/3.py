# 149p

def solution(n, m, a):
    ctr = 0
    for i in range(n):
        for j in range(m):
          if dfs(i, j, a) == True:
              ctr += 1  
    return ctr

def dfs(x, y, a):
    if x>=n or x<=-1 or y>=m or y<=-1:
        return False
    if a[x][y] == 0:
        a[x][y] = 1
        dfs(x-1, y, a)
        dfs(x+1, y, a)
        dfs(x, y-1, a)
        dfs(x, y+1, a)
        return True
    return False

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input())))
print(solution(n, m, a))