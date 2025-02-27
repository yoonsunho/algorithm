xi = [-1, 0, 1, 0]
xj = [0, 1, 0, -1]

# 백준 14503

def cleaning(i, j, di):

    cnt = 0
    while True:
        # 현재 위치 청소
        room[i][j] = 2
        cnt += 1

        flag = 1
        while flag == 1:
            for nd in [(di+3) % 4, (di+2) % 4, (di+1) % 4, di]:
                ni, nj = i + xi[nd], j + xj[nd]
                if room[ni][nj] == 0:     # 미청소 영역
                    i, j, di = ni, nj, nd
                    flag = 0
                    break
        else:   # 4방향 모두 미청소 영역 없음
            ni = i - xi[di]     # 후진할 위치 계산
            nj = j - xj[di]
            if room[ni][nj] == 1:   # 벽 => 종료
                return cnt
            else:
                i, j = ni, nj


N, M = map(int, input().split())

st_i, st_j, direction = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

ans = cleaning(st_i, st_j, direction)

print(ans)
