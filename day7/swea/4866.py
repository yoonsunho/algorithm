import sys
sys.stdin = open("txt/4866.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    txt = input()
    stack = [0] * 100
    top = -1
    ans = 0

    for x in txt:
        if txt == '{':
            top += 1
            stack[top] = '{'
        elif txt == '}':
            if top == -1:
                ans = 0
                break
            else:
                top -= 1
                stack.pop()



    print(f'{test_case}')