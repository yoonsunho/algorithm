import sys
sys.stdin = open("txt/1974.txt", "r")

# 15m
T = int(input())

for tc in range(1, T+1):

    matrix = [list(map(int,input().split())) for _ in range(9)]

    ans = 1
    for i in range(3):
        for j in range(3):
            cnt = 0
            for k in range(3):
                for l in range(3):
                    cnt += matrix[i*3+k][j*3+l]
            if cnt != 45:
                ans = 0
                break

    for _ in range(2):
        for i in range(9):
            cnt = 0
            for j in range(9):
                cnt += matrix[i][j]
            if cnt != 45:
                ans = 0
                break
        matrix = list(map(list, zip(*matrix)))

    print(f'#{tc} {ans}')