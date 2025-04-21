# 0421(월)
# 16637.. 괄호 추가하기 (골드3)
# gpt참조함


def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    else:
        return n1 * n2


def dfs(i, value):

    global max_v

    if i == len(oper):
        max_v = max(max_v, value)
        return

    # 연산자 바로 다음에 괄호 없는 경우
    next_value = calc(value, num_list[i+1], oper[i])
    dfs(i+1, next_value)

    # 연산자 바로 다음에 괄호 있는 경우(현재 연산자 다음에 연산자 있어야됨)
    if i+1 < len(oper):
        # 괄호 연산 먼저 하기
        brace_result = calc(num_list[i+1], num_list[i+2], oper[i+1])
        next_value = calc(value, brace_result, oper[i])
        # i+2로 해줌으로써 괄호 중복 방지
        dfs(i+2, next_value)

N = int(input())    # 수식의 길이(1 ≤ N ≤ 19)
susik = input()     # 주어진 수식

num_list = []
oper = []
for i in range(N):
    if i % 2 == 0:
        num_list.append(int(susik[i]))
    else:
        oper.append(susik[i])
# print(num_list)
# print(oper)
max_v = -float('inf')
dfs(0, num_list[0])

print(max_v)




