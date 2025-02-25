import sys
sys.stdin = open("txt/9386.txt","r")

# 10m
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input()))

    max_l = 0
    cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            max_l = max(cnt, max_l)
        else:
            cnt = 0


    print(f'#{tc} {max_l}')