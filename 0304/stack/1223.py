import sys
sys.stdin = open("txt/1223.txt", "r")

icp = {"+": 1, "*":2}
isp = {"+": 1,"*":2}

for tc in range(1,11):

    N = int(input())
    fx = input()

    stack = [0] * N
    top = -1
    susik = ''

    for x in fx:
        if x not in "+*":
            susik += x
        else:
            if top == -1 or icp[x] > isp[stack[top]]:
                top += 1
                stack[top] = x
            elif icp[x] <= isp[stack[top]]:
                while top > -1 and icp[x] <= isp[stack[top]]:
                    susik += stack[top]
                    top -= 1
                top += 1
                stack[top] = x

    while top > -1:
        susik += stack[top]
        top -= 1

    # print(susik)
    # print(top)
    new_stack = [0]*N

    for x in susik:
        if x not in  "+*":
            top += 1
            new_stack[top] = int(x)
        elif x == "+":
            op2 = new_stack[top]
            top -= 1
            op1 = new_stack[top]
            new_stack[top] = int(op1) + int(op2)
        elif x == "*":
            op2 = new_stack[top]
            top -= 1
            op1 = new_stack[top]
            new_stack[top] = int(op1) * int(op2)

    # print(top)

    print(f'#{tc} {new_stack[top]}')