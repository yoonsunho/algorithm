import sys
sys.stdin = open("txt/21617.txt", "r")

T = int(input())
for tc in range(1, T+1):

    txt = input()

    top = -1
    stack = [0] * 1000
    ans = 1
    for x in txt:
        if x == "(" or x == "{":
            top += 1
            stack[top] = x
        elif x == ")" or x == "}":
            if x == ")":
                if stack[top] != "(":
                    ans = 0
                else:
                    top -= 1
            elif x == "}":
                if stack[top] != "{":
                    ans = 0
                else:
                    top -= 1
    if top != -1:
        ans = 0




    print(f'#{tc} {ans}')