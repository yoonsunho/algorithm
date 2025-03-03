import sys
sys.stdin = open("txt/5097.txt", "r")

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    front, rear = -1, -1

    new_arr = [0] * N
    for _ in range(M):
        for i in range(N):
            new_arr[i] = arr[(i+1) % N]
        arr = new_arr[:]



    print(f'#{tc} {new_arr[0]}')