import sys
sys.stdin = open("txt/11092.txt", "r")

# 6m
T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        elif arr[max_idx] <= arr[i]:
            max_idx = i

    ans = abs(max_idx - min_idx)



    print(f'#{tc} {ans}')