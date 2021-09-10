
def solution(n, a):
    x, y = 1, 1
    
    for i in a:
        if i == 'R':
            if x == n:
                continue
            x += 1
        elif i == 'L':
            if x == 1:
                continue
            x -= 1
        elif i == 'U':
            if y == 1:
                continue
            y -= 1
        elif i == 'D':
            if y == n:
                continue
            y += 1
    print(y, x)


n = int(input())
a = input().split()

solution(n, a)