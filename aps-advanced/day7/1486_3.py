import sys
sys.stdin = open("txt/1486.txt", "r")

def recur(n,total):
    global min_hei

    if n == N:
        if total >= S:
            min_hei = min(min_hei, total)
        return

    recur(n+1, total)
    recur(n+1, total+hei[n])

T = int(input())
for tc in range(1, T+1):

    N, S = map(int, input().split())
    hei = list(map(int, input().split()))

    min_hei = float('inf')
    recur(0,0)

    print(f'#{tc} {min_hei-S}')