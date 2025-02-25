import sys
sys.stdin = open("txt/6485.txt", "r")

T = int(input())

for tc in range(1, T+1):

    N = int(input())    # 버스 노선의 개수 1 ≤ N ≤ 500
    st = [0] * N
    end = [0] * N
    for i in range(N):
        st[i], end[i] = map(int, input().split())

    P = int(input())    # 버스정류장의 수 1 ≤ P ≤ 500

    c = [0] * P

    for i in range(P):
        c[i] = int(input())

    count = [0] * P

    for i in range(N):
        for j in range(P):
            if st[i] <= c[j] <= end[i]:
                count[j] += 1


    print(f'#{tc} {" ".join(map(str,count))}')