xi = [-1, 0, 1, 0]
xj = [0, 1, 0, -1]

def cleaning(i, j, di, cnt):

    # 현재 위치 청소
    room[i][j] = 2
    cnt += 1

    di = (di + 3) % 4
    for k in range(4):
        di = (di + k) % 4
        ni = i + xi[di]
        nj = j + xj[di]
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj]==0:     # 미청소 영역
            return cleaning(ni, nj, di, cnt)
    else:
        di = (di+2) % 4     # 후진 방향 
        ni = i + xi[di]
        nj = j + xj[di]
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] != 1:
            return cleaning(ni, nj, di, cnt)
        else:
            return cnt




N, M = map(int, input().split())

st_i, st_j, direction = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

count = 0

ans = cleaning(st_i, st_j, direction, count)

print(ans)
