import sys
sys.stdin = open("txt/21619.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    txt = input()   # 입력받기
    top = -1
    stack = [0] * 100
    ans = 1
    for x in txt:
        if x == '(':
            top += 1
            stack[top] = x
        elif x == ')':
            if top == -1:
                ans = -1
                break
            else:
                top -= 1

    if top != -1:   # 열린 괄호 남아있으면
        ans = -1



    print(f'#{test_case} {ans}')