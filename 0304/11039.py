import sys
sys.stdin = open("txt/11039.txt", "r")

# 48m

def check(x,y,n):
    wid, hei = 1, 1
    for k in range(1, n-y):
        if matrix[x][y+k] == 1:
            wid += 1
        else:
            break
    for k in range(1, n-x):
        if matrix[x+k][y] == 1:
            hei += 1
        else:
            break
    return wid * hei


T = int(input())
for tc in range(1, T+1):

    N = int(input())        # N x N 배열 사각형

    matrix = [list(map(int, input().split())) for _ in range(N)]


    max_v = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 and (j == 0 or matrix[i][j-1] == 0) and (i == 0 or matrix[i-1][j] == 0):
                ans = check(i, j, N)
                max_v = max(max_v, ans)





    print(f'#{tc} {max_v}')