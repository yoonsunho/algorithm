import sys
sys.stdin = open("txt/1222.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    result = ''
    stack = [0]*N
    top = -1

    fx = input()
    for x in fx:
        if x != '+':        # 피연산자
            result += str(x)
        else:               # 연산자라면(+)
            if top == -1:   # stack이 비어있음
                top += 1    #push
                stack[top] = x

            else:           # stack 이 비어있지 않음 (+들어있음)
                result += str(stack[top])
                top -= 1
                top += 1
                stack[top] = x


    result += stack[top]
    top -= 1

    stack = [0]*N

    for s in result:
        if s != '+':    # 피연산자라면 stack에 푸쉬
            top += 1
            stack[top] = int(s)
            # print(stack)
        else:       # 연산자라면

            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            ans = op1 + op2
            top += 1
            stack[top] = ans

    print(f'#{test_case} {stack[top]}')