import sys
sys.stdin = open("txt/1210.txt", "r")

di = [0,0,-1]
dj = [1,-1,0]

def going_up(i,j):

    pass





for _ in range(10):

    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        if ladder[99][j] == 2:
            st_i, st_j = 99, j

    # print(st_i,st_j)

    ans = going_up(st_i,st_j)

    print(f'#{tc} {ans}')

