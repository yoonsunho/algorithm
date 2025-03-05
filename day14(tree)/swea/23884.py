import sys
sys.stdin = open("txt/23884.txt", "r")

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        # print(node[n], end=" ")
        ans.append(node[n])


for tc in range(1, 11):

    N = int(input())    # 정점의 개수
    left = [0] * (N+1)
    right = [0] * (N+1)
    node = [0] * (N+1)  # 각 노드의 값들을 담을 배열
    # print(node)
    ans = []

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

    # print(left)
    # print(right)
    post_order(1)
    # print(node)
    # print(ans)
    stack = [0] * 1000
    top = -1
    # print(ans)
    for x in ans:
        if x not in ['+', '-', '*', '/']:
            top += 1
            stack[top] = x
        else:
            op2 = stack[top]  # pop(), 오른쪽 피연산자
            # print(type(op2))
            top -= 1
            op1 = stack[top]  # pop(), 왼쪽 피연산자
            # print(type(op1))
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '-':
                top += 1
                stack[top] = op1 - op2
            elif x == '*':
                top += 1
                stack[top] = int(op1 * op2)
            elif x == '/':
                top += 1
                stack[top] = int(op1 / op2)

    # print(stack)
    print(f'#{tc} {stack[top]}')