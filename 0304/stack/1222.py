import sys
sys.stdin = open("txt/1222.txt", "r")

for tc in range(1, 11):

    N = int(input())
    fx = input()
    stack = [0] * N
    susik = ''
    top = -1

    for x in fx:
        if x != "+":
            susik += x
        elif x == "+":
            if top > -1:
                susik += x
            else:
                top += 1
                stack[top] = x

    if top > -1:
        susik += stack[top]
        top -= 1

    # print(susik)
    # print(top)

    new_stack = [0] * 256
    for x in susik:
        if x != "+":
            top += 1
            new_stack[top] = x
        elif x == "+":
            op2 = new_stack[top]
            top -= 1
            op1 = new_stack[top]
            new_stack[top] = int(op1) + int(op2)

    # print(top)
    # print(new_stack[top])





    print(f'#{tc} {new_stack[top]}')