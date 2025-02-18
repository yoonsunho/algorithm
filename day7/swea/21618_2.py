# import sys
# sys.stdin = open("txt/21618.txt", "r")

# 예영언니가 도와줌

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    txt = input()
    N = len(txt)  # 1<=N<=1000

    stack = [txt[0]]
    top = 0

    for i in range(1,N):
        if len(stack) == 0:
            top += 1
            stack.append(txt[i])
        elif txt[i] == stack[top]:
            stack.pop()
            top -= 1
        else:
            top += 1
            stack.append(txt[i])





    print(f'#{test_case} {len(stack)}')