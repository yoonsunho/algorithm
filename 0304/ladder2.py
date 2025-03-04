import sys
sys.stdin = open("list2/txt/1211.txt", "r")

di = [1, 0, 0]
dj = [0, 1, -1]

def search_ladder(x,y):

    visited = [[0] * 100 for _ in range(100)]
    visited[x][y] = 1
    count = 0
    global min_x, min_y

    while x != 99:

        for k in range(3):
            ni, nj = x + di[k], y + dj[k]

            # 범위 밖인 경우 제외
            if ni < 0 or ni >= 100 or nj < 0 or nj >= 100:
                continue

            # 사다리가 아닌경우 ㅈ외
            if ladder[ni][nj] == 0:
                continue

            # 방문한 경우 제외
            if visited[ni][nj] == 1:
                continue

            count += 1
            visited[ni][nj] = 1
            x, y = ni, nj

    return count


for _ in range(10):

    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    max_cnt = 0
    for j in range(100):
        if ladder[0][j] == 1:
            min_count = 100000
            min_x, min_y = -1, -1
            cnt = search_ladder(0, j)
            # max_cnt = max(cnt, max_cnt)

    print(f'#{tc} {cnt}')