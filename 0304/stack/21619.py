import sys
sys.stdin = open("txt/21619.txt", "r")

T = int(input())
for tc in range(1, T+1):

    txt = input()

    stack = [0] * 100
    top = -1
    ans = 1

    for x in txt:
        if x == "(":
            top += 1
            stack[top] = "("
        elif x == ")":
            if top == -1:
                ans = -1
            top -= 1

    if top > -1:
        ans = -1


    print(f'#{tc} {ans}')