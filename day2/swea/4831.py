import sys
sys.stdin = open("txt/4831.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    now_idx = 0
    i = 0
    cnt = 0

    while now_idx + K < N:
        next_stop = now_idx

        while i < M and bus_stop[i] <= now_idx + K:
            next_stop = bus_stop[i]
            i += 1

        if next_stop == now_idx:
            cnt = 0
            break

        now_idx = next_stop
        cnt += 1


    print(f'#{test_case} {cnt}')