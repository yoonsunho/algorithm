import sys
sys.stdin = open("txt/5174.txt" , "r")

def count_order(n):
    global cnt
    if n:
        cnt += 1
        count_order(left[n])
        count_order(right[n])
    return cnt

T = int(input())
for tc in range(1, T+1):

    E, N = map(int, input().split())        # E: 간선의 개수 , N: 노드의 숫자
    V = E + 1   # 정점의 개수

    arr = list(map(int, input().split()))
    left = [0] * (V+1)      # 왼 자식 모음
    right = [0] * (V+1)     # 우 자식 모음
    par = [0] * (V+1)

    for i in range(E):
        p, c = arr[2 * i], arr[2*i+1]
        par[c] = p
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # print(par)
    # print(left)
    # print(right)

    # 루트 찾기
    for i in range(1, V+1):
        if par[i] == 0:
            root = i
            break

    cnt = 0
    ans = count_order(N)



    print(f'#{tc} {ans}')