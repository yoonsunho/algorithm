import sys
sys.stdin = open("txt/5248.txt", "r")

T = int(input())

for tc in range(1,T+1):

    N, M = map(int, input().split())    #  출석번호, 신청서 갯수(2<=N<=100, 1<=M<=100)

    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(N+1) ]
    for i in range(M):
        s,e = arr[2*i], arr[2*i+1]
        adj_list[s].append(e)
        adj_list[e].append(s)

    print(adj_list)
    print(f'#{tc}')