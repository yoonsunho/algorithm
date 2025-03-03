import sys
sys.stdin = open("txt/4874.txt", "r")

T = int(input())
for tc in range(1, T+1):

    susik = list(input().split())     # 256자 이내
    top = -1
    stack = [0] * 256

    result = "error"

    for x in susik:
        if x not in '+-*/.':
            top += 1
            stack[top] = int(x)
        if x in "+-*/":
            if top < 1:
                break
            elif x == "+":
                op2 = stack.pop(top)
                top -= 1
                op1 = stack.pop(top)
                stack[top] = op1 + op2
            elif x == "-":
                op2 = stack.pop(top)
                top -= 1
                op1 = stack.pop(top)
                stack[top] = op1 - op2
            elif x == "*":
                op2 = stack.pop(top)
                top -= 1
                op1 = stack.pop(top)
                stack[top] = int(op1 * op2)
            elif x == "/":
                op2 = stack.pop(top)
                top -= 1
                op1 = stack.pop(top)
                stack[top] = int(op1 / op2)
        elif x == ".":
            if top == 0:
                result = stack[top]





    print(f'#{tc} {result}')