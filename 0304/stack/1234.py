import sys
sys.stdin = open("txt/1234.txt","r")

for tc in range(1, 11):

    N, pwd = input().split()
    N = int(N)

    stack = [0]*100
    top = 0
    stack[0] = pwd[0]

    for i in range(1, N):
        if stack[top] != pwd[i]:
            top += 1
            stack[top] = pwd[i]
        else:
            top -= 1




    print(f'#{tc}',end=" ")
    for i in range(top+1):
        print(stack[i],end="")
    print()