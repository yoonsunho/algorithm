import sys
sys.stdin = open("txt/21673.txt", "r")

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}   # 토큰의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}   # 스택내부에서의 우선순위


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    susik = input()

    stack = []
    str = ''
    top = -1

    for s in susik:
        if s not in '(+_*/)': # 숫자면
            str += s
        elif s == ")":
            while stack[top] != "(":
                str += stack[top]
                top -= 1




    print(f'#{test_case}')