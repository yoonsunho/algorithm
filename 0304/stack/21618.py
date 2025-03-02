import sys
sys.stdin = open("txt/21618.txt","r")

T = int(input())
for tc in range(1, T+1):

    txt = input()

    top = -1
    stack = [0] * 1000
    for x in txt:
        if x != stack[top]:
            top += 1
            stack[top] = x
        else:
            stack.pop(top)
            top -= 1

    print(f'#{tc} {top+1}')