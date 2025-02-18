import sys
sys.stdin = open("pari.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    pari_arr = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += pari_arr[i+k][j+l]
            max_v = max(max_v, sum)
    print(f'#{tc} {max_v}')