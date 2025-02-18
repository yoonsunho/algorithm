import sys
sys.stdin = open("txt/input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, num = input().split()
    N = int(N)
    number = str(num)

    stack = []
    top = 0
    stack.append(number[0])

    for i in range(1, N):
        # if top < 0:
        #     top = 0
        if len(stack) == 0:
            top += 1
            stack.append(number[i])
        elif stack[top] != number[i]:
            top += 1
            stack.append(number[i])
        elif stack[top] == number[i]:
            top -= 1
            stack.pop()








    print(f'#{test_case} {"".join(stack)}')