import sys
sys.stdin = open("txt/1206.txt", "r")

# 8M 16S
T = 10
for tc in range(1, T+1):

    N = int(input())        # 4 ≤ N ≤ 1000)

    hei = list(map(int, input().split()))       # 0 ≤ 각 건물의 높이 ≤ 255

    count = 0
    for i in range(2, N-2):
        max_v = max(hei[i-2], hei[i-1], hei[i+1], hei[i+2])
        if max_v < hei[i]:
            count += (hei[i] - max_v)

    print(f'#{tc} {count}')