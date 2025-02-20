import sys
sys.stdin = open("txt/4874.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    fx = input().split()
    print(fx)
    stack = [0] * 256
    top = -1

    for x in fx:
        if x not in '+-*/.':     # 피연산자라면
            # count_num
            top += 1
            stack[top] = int(x)
        elif x not in ".":
            if stack[0] != 0 and stack[1] != 0:
                op2 = stack[top]
                stack[top] = 0
                top -= 1
                op1 = stack[top]
                stack[top] = 0
                top -= 1
                if x == "+":
                    a = op1 + op2
                elif x == "*":
                    a = op1 * op2
                elif x == "/":
                    a = op1 / op2
                elif x == "-":
                    a = op1 - op2
                top += 1
                stack[top] = a

            else:
                ans = 'error'
        else:        # 연산자라면

            ans = stack[top]
            break


    print(f'#{test_case} {ans}')