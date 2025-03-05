import sys
sys.stdin = open("txt/23880.txt", "r")

def in_order(n):
    if n:
        in_order(left[n])
        print(node[n], end="")
        in_order(right[n])


for tc in range(1, 11):

    N = int(input())        # 정점의 수
    E = N - 1               # 간선의 수

    node = ['a'] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)


    for _ in range(N):
        arr = list(input().split())
        i = int(arr[0])
        node[i] = arr[1]
        if len(arr) == 3:
            left[i] = int(arr[2])
        elif len(arr) == 4:
            left[i] = int(arr[2])
            right[i] = int(arr[3])

    # print(left)
    # print(right)
    # print(node)

    # in_order(1)

    print(f'#{tc} ',end='')
    in_order(1)
    print()