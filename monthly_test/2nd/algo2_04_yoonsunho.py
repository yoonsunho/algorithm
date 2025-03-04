'''
3
5
1 1 1 1 1
1 2 0 0 1
1 0 1 0 1
1 0 3 0 1
1 1 1 1 1
5
1 1 1 1 1
1 2 0 4 1
1 1 1 1 1
1 0 3 0 1
1 1 1 1 1
5
1 1 1 1 1
1 2 1 0 1
1 4 3 0 1
1 0 1 0 1
1 1 1 1 1

'''
di = [0,1,0,-1]
dj = [1,0,-1,0]

def miro_count(i,j):
    x, y = i, j
    count = 1

    while miro[x][y] != 3:

        next_i, next_j = -1, -1
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if miro[ni][nj] == 0:
                    miro[x][y] = 4
                    next_i, next_j = ni, nj
                elif miro[ni][nj] == 3:
                    next_i, next_j = ni, nj
                    break

        if next_i == -1:
            count = -1
            break

        x, y = next_i, next_j
        count += 1

    return count


def find_start():       # 시작위치 찾는 함수
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                return i, j
T = int(input())

for tc in range(1, T+1):

    N = int(input())        # 미로의 크기 (5<=N<=15)

    miro = [list(map(int,input().split())) for _ in range(N)]

    st_i, st_j = find_start()

    # adj_list = [[]]

    ans = miro_count(st_i,st_j)




    print(f'#{tc} {ans}')
