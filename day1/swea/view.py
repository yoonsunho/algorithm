import sys
sys.stdin = open("view.txt", "r")

T = 10

for tc in range(1, T+1):
    N = int(input())    # 건물의 개수
    hei = list(map(int, input().split()))

    # min_v = 0
    count = 0
    for i in range(2, N-2):
        if hei[i] > 0:
            if hei[i] > hei[i-2] and hei[i] > hei[i-1] and hei[i] > hei[i+1] and hei[i] > hei[i+2]:
                min_v = hei[i] - hei[i-2]
                for j in range(i-1, i+3):
                    if j != i and min_v > hei[i] - hei[j]:
                        min_v = hei[i] - hei[j]
                count += min_v

    print(f'#{tc} {count}')