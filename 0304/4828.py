import sys
sys.stdin = open("txt/4828.txt","r")

# 4m 50s
T = int(input())
for tc in range(1, T+1):

    N = int(input())

    a = list(map(int, input().split()))

    max_n = a[0]
    min_n = a[0]
    for i in range(1,N):
        if a[i] > max_n:
            max_n = a[i]
        elif a[i] < min_n:
            min_n = a[i]

    ans = max_n-min_n

    print(f'#{tc} {ans}')