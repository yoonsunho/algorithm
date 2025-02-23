import sys
sys.stdin = open("txt/4874.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    fx = input().split()
    # print(fx)
    stack = [0] * 256
    top = -1

    for x in fx:
        if x not in '+-*/.':     # 피연산자라면(숫자)
            # count_num
            top += 1
            stack[top] = int(x)
        elif x != ".":
            if top > 0:
                op2 = int(stack[top])
                stack[top] = 0
                top -= 1
                op1 = int(stack[top])
                stack[top] = 0
                top -= 1
                if x == "+":
                    a = int(op1 + op2)
                elif x == "*":
                    a = int(op1 * op2)
                elif x == "/":
                    a = int(op1 // op2)
                elif x == "-":
                    a = int(op1 - op2)
                elif x == "%":
                    a = int(op1 % op2)
                top += 1
                stack[top] = a

            else:
                ans = 'error'
                break
        else:        # . 라면
            ###################여기 조건 주의!!!!!!!!!!!
            if top == 0:
                ans = stack[top]
            else:
                ans = 'error'



    print(f'#{test_case} {ans}')