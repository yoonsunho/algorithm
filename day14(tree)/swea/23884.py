import sys
sys.stdin = open("txt/23884.txt", "r")

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end="")


for tc in range(1, 11):

    N = int(input())    # 정점의 개수
    left = [0] * (N+1)
    right = [0] * (N+1)
    node = [0] * (N+1)  # 각 노드의 값들을 담을 배열
    # print(node)

    for _ in range(N):
        arr = list(input().split())
        # print(arr)
        i = int(arr[0])
        if len(arr) == 2:
            node[i] = int(arr[1])
        else:       # 연산자 들어있을 때
            node[i] = arr[1]
            left[i] = int(arr[2])
            right[i] = int(arr[3])

    print(left)
    print(right)
    post_order(1)
    print(node)

    print(f'#{tc} ')