import sys
sys.stdin = open("txt/23417.txt", "r")

# 7m
T = int(input())

for tc in range(1, T+1):

    N = int(input())
    hei = list(map(int, input().split()))

    max_cnt = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if hei[i] > hei[j]:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    print(f'#{tc} {max_cnt}')