import sys
sys.stdin = open("samsung_bus.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 버스 노선의 개수
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())  # i번째 노선 A번 이상의 B번 이하의정류장 지나감

    P = int(input())    # p개의 버스 정류장
    # C1 = int(input())   # 각 정류장의 번호#1
    C = [0] * P

    for i in range(P):
        C[i] = int(input())

    bus_stop = [0]* 5000

    for i in C:
        for j in range(A[0],A[N-1]+1):
            if i == j:
                bus_stop[i] += 1
        for j in range(B[0],B[N-1]+1):
            if i == j:
                bus_stop[i] += 1

    print(bus_stop)


    print(f'#{test_case} ')