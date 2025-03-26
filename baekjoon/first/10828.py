# 스택
import sys
input = sys.stdin.readline  # 시간 초과 문제 해결

N = int(input())    # 명령의 개수 (1 ≤ N ≤ 10,000)
stack = [0] * 10000
top = -1

for _ in range(N):
    x = input().strip() # 개행 제거를 위해 필요

    if x == "pop":
        if top > -1:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif x == "size":
        print(top+1)
    elif x == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif x == "top":
        if top > -1:
            print(stack[top])
        else:
            print(-1)
    else:   # push 일 경우
        top += 1
        stack[top] = int(x[5:])
