import sys
sys.stdin = open("txt/4831.txt", "r")

T = int(input())

for test_case in range(1,T+1):

    K, N, M = map(int, input().split())     # k:한번 충전으로 갈수 있는 최대 정류장 
    bus_stop = list(map(int, input().split()))

    cnt = 0
    i = 0
    now_stop = 0   # 버스의 현위치
    
    # 현 위치에서 k 만큼 더한게 마지막 정류장보다 작을 때 까지 반복
    while now_stop + K < N:
        next_stop = now_stop    # 다음 위치에 현위치 넣어주기 (변수 초기화)

        while i < M and bus_stop[i] <= now_stop + K:    # i는 bus_stop의 인덱스 , 현위치 보다 k만큼 큰것 중에 가장 큰 아이를 뽑을 수 있게 함 
            next_stop = bus_stop[i] # 다음정류장 갱신
            i += 1

        if next_stop == now_stop:   # 위의 while문이 실행 안된경우, 즉 현 위치에서 k 만큼 더한 것 내에 bus_stop이 없을때, 종료
            cnt = 0
            break

        now_stop = next_stop # 현 위치에 다음정류장으로 업데이트
        cnt += 1


    print(f'#{test_case} {cnt}')

