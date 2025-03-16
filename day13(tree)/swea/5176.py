import sys
sys.stdin = open("txt/5176.txt", "r")

def in_order(n):
    global cnt
    if n:
        in_order(left[n])
        cnt += 1
        arr[n] = cnt
        in_order(right[n])

T = int(input())
for tc in range(1, T+1):

    N = int(input())      # 정점의 수
    E = N - 1            # 간선의 수

    arr = [0]*(N+1)
    # print(arr)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N//2+1):
        l, r = 2 * i, 2 * i+1
        if l <= N:
            left[i] = l
        if r <= N:
            right[i] = r
    # print(left)
    # print(right)
    cnt = 0

    in_order(1)
    # print(arr)


    print(f'#{tc} {arr[1]} {arr[N//2]}')