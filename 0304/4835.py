import sys
sys.stdin = open("txt/4835.txt","r")

# 18m

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())     # 10 ≤ N ≤ 100,  2 ≤ M ＜ N

    arr = list(map(int, input().split()))       # 1 ≤ a ≤ 10000

    min_v , max_v = 0, 0
    for i in range(M):
        min_v += arr[i]
        max_v += arr[i]

    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += arr[i+j]
        max_v = max(sum, max_v)
        min_v = min(sum, min_v)

    ans = max_v- min_v






    print(f'#{tc} {ans}')