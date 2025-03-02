import sys
sys.stdin = open("txt/21673.txt","r")

T = int(input())
for tc in range(1, T+1):

    icp = {"+":1,"-":1, "*":2, "/" : 2}
    isp = {"+":1,"-":1, "*":2, "/" :2}

    fx = input()
    susik = ''
    top = -1
    stack = [0]*1000

    for x in fx:
        if x not in '+-*/':
            susik += x
        else:       # 연산자
            if top == -1 or isp[stack[top]] < icp[x]:       # 스택 비어있거나 토큰의 우선순위가 높을 때
                top += 1
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1
                stack[top] = x

    while top > -1:
        susik += stack[top]
        top -= 1


    print(f'#{tc} {susik}')