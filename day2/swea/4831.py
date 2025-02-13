import sys
sys.stdin = open("txt/4831.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    cnt = 0
    if bus_stop[0] > N or N - K > bus_stop[M-1]:
        cnt = 0

    new_bus_list = [0]
    new_bus_list.extend(bus_stop)
    new_bus_list.append(N)

    arr = []

    for i in range(M):
        max_v = 0
        for j in range(i+1, M+1):
            if new_bus_list[j] - new_bus_list[i] <= K:
                max_v = new_bus_list[j]
                break
        else:
            cnt = 0

        arr.append(max_v)
        print(arr)
        # while bus_stop[i+1] - bus_stop[i] <= K:
        #     max_v = i
        # arr.append(max_v)
        # print(arr)



    # for i in range(N-1):
    #     if bus_stop[i+1] - bus_stop[i] > N:
    #         cnt = 0
    #
    #





    print(f'{test_case} {cnt}')