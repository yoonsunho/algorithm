import sys
sys.stdin = open("txt/ladder.txt", "r")
# greedy

def check(x, y):

    # 지나가는 곳의 좌표 0으로 변경( 두번 지날일 없으므로 ㄱㅊ)
    ladder_arr[x][y] = 0

    while x != 0:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 새로운 x,y좌표가 범위값 안에있고
            # 사다리에 해당값이 존재할 떄,(파이썬에서 0: false로 인식, 0제외는 true로 인식)
            if 0 <= nx < 100 and 0 <= ny < 100 and ladder_arr[nx][ny]:
                ladder_arr[nx][ny] = 0
                x, y = nx, ny
    return y


for _ in range(10):
    T = int(input())

    ladder_arr = [list(map(int,input().split())) for _ in range(100)]

    dx = [-1, 0, 0]
    dy = [0, -1, 1]

    for j in range(100):
        if ladder_arr[99][j] == 2:
            ans = check(99, j)

    print(f'#{T} {ans}')