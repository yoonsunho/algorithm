import sys
sys.stdin = open("txt/5178.txt", "r")

def sum_node(n):
    global last
    c = last
    p = c // 2
    while p >= 1:
        if c % 2 == 0:  # last 가 짝수일 때
            arr[p] = arr[c]
            c -= 1
            p = c // 2
        else:
            arr[p] = arr[c] + arr[c-1]
            c -= 2
            p = c // 2

    return arr[L]

T = int(input())
for tc in range(1,T+1):

    N, M, L = map(int,input().split())      # 노드 개수, 리프노드 개수, 출력할 노드 번호

    arr = [0] * (N+1)       # 전체 노드별 값을 담을 배열

    for _ in range(M):

        i, v = map(int, input().split())

        arr[i] = v

    # print(arr)

    last = N
    ans = sum_node(1)

    print(f'#{tc} {ans}')