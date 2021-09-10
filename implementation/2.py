
def solution(p):
    ctr = 0

    x = int(ord(list(p)[0])) - int(ord('a')) + 1
    y = int(list(p)[1])

    if x-2 >= 1 and y-1 >= 1:
        ctr += 1
    if x-2 >= 1 and y+1 <= 8:
        ctr += 1
    if x+2 <= 8 and y-1 >= 1:
        ctr += 1
    if x+2 <= 8 and y+1 <= 8:
        ctr += 1
    if x-1 >= 1 and y-2 >= 1:
        ctr += 1
    if x+1 <= 8 and y-2 >= 1:
        ctr += 1
    if x-1 >= 1 and y+2 <= 8:
        ctr += 1
    if x+1 <= 8 and y+2 <= 8:
        ctr += 1

    return ctr

p = input()
print(solution(p))