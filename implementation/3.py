# 118p
# 0: north, 1: east, 2: south, 3: west

def solution(n, m, a, b, d, mp):
    ctr = 1
    t = 0
    able = True
    
    v = [(a, b)]
    # mv = [()]
    
    d = (d+3) % 4
    while able:
        # print(f'ctr: {ctr}, v: {v}, d: {d}, t: {t}')
        d = (d+3) % 4
        if d == 0:
            if mp[a-1][b] != 1 and (a-1, b) not in v:
                a -= 1
                b = b
                v.append((a, b))
                ctr += 1
                t = 0
            else:
                t += 1
        elif d == 3:
            if mp[a][b-1] != 1 and (a, b-1) not in v:
                a = a
                b -= 1
                v.append((a, b))
                ctr += 1
                t = 0
            else:
                t += 1
        elif d == 2:
            if mp[a+1][b] != 1 and (a+1, b) not in v:
                a += 1
                b = b
                v.append((a, b))
                ctr += 1
                t = 0
            else:
                t += 1
        elif d == 1:
            if mp[a][b+1] != 1 and (a, b+1) not in v:
                a = a
                b += 1
                v.append((a, b))
                ctr += 1
                t = 0
            else:
                t += 1
        
        if t == 4:
            if d == 0 and mp[a+1][b] != 1:
                a += 1
                b = b
                t = 0
                continue
            if d == 3 and mp[a][b+1] != 1:
                a = a
                b += 1
                t = 0
                continue
            if d == 2 and mp[a-1][b] != 1:
                a -= 1
                b = b
                t = 0
                continue
            if d == 1 and mp[a-1][b] != 1:
                a -=1 
                b = b
                t = 0
                continue
            return ctr

n, m = map(int, input().split())
a, b, d = map(int, input().split())
mp = []
for i in range(n):
    mp.append(list(map(int, input().split())))

print(solution(n, m, a, b, d, mp))