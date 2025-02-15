import sys
sys.stdin = open("samsung_bus.txt", "r")
'''
1
2
1 3
2 5
5
1
2
3
4
5
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 버스 노선의 개수
    st_num = [0] * N      # 버스 노선별 시작 정류장의 번호를 담을 배열
    end_num = [0] * N      # 버스 노선 별 종료 정류장의 번호를 담을 배열
    for i in range(N):
        st_num[i], end_num[i] = map(int, input(). split())

    P = int(input())    # 버스정류장의 개수
    bus_stop = [0] * P
    for i in range(P):
        bus_stop[i] = int(input())      # 1 2 3 4 5

    cnt = {}  # 각 정류장을 지나는 노선수를 담을 새로운 딕셔너리

    for stop in bus_stop:
        cnt[stop] = 0

    for i in range(N):
        for k in range(st_num[i], end_num[i]+1):
            if k in cnt:        # 주어진 범위 내가 정류장이 P가 있을 떄
                cnt[k] += 1

    ans = []
    for stop in bus_stop:
        ans.append(cnt[stop])

    print(f'#{test_case} {" ".join(map(str,ans))}')