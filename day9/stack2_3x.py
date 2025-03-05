top = -1
stack = [0] * 100

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}   # 토큰의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}   # 스택내부에서의 우선순위


fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '+-*/':
        susik += x
    elif x == ")":
        while stack[top] != '(':    # '(' 까지  pop()
            susik += stack[top]     # peek
            top -= 1
        top -= 1    # '(' 버림.pop
    else:
        pass

susik = '6528-*2/+'


for x in susik:
    if x not in '+-/*':     # 피연산자면
        top += 1
        stack[top] = int(x)
    else:       # 연산자면
        op2 = stack[top]    # pop(), 오른쪽 피연산자
        top -= 1
        op1 = stack[top]    # pop(), 왼쪽 피연산자
        top -= 1
        if x == '+':
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2

print(stack[top])
