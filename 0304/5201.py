import sys
sys.stdin = open("txt/5201.txt", "r")

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())     # 컨테이너 수, 트럭수


    container = sorted(list(map(int, input().split())))[::-1]
    truck = sorted(list(map(int, input().split())))[::-1]

    # print(container,truck)

    new_arr = []

    if N <= M:
        new_truck = truck[0:N]
        # print(new_truck)
        for i in range(N):
            if container[i] <= new_truck[0]:
                new_truck.pop(0)
                new_arr.append(container[i])
                if truck == []:
                    break
    else:
        for i in range(N):
            if container[i] <= truck[0]:
                truck.pop(0)
                new_arr.append(container[i])
                if truck == []:
                    break


    # print(sum(new_arr))
    if new_arr == []:
        ans = 0
    else:
        ans = sum(new_arr)



    print(f'#{tc} {ans}')