# 다리 끼리 겹칠 수 없음
# McN을 구하는 문제임(조합)
# 시간 초과
# dp로 풀어 볼까


def recur(cnt, start):

    global ans
    if cnt == N:
        ans += 1
        return

    for i in range(start,M):
        path.append(i)
        recur(cnt +1, i +1)
        path.pop()


T = int(input())
for _ in range(T):

    N, M  = map(int, input().split())

    ans = 0
    path = []
    recur(0,0)
            

    print(f'{ans}')