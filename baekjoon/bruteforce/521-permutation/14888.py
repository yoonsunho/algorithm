# 0404(금) 연산자 끼워넣기
# 실버 1

def calc(arr):
    # global min_num, max_num
    n_list = num_list[:]
    for i in range(N-1):
        num1 = n_list.pop(0)
        num2 = n_list[0]
        # print(num2)
        if arr[i] == '+':
            n_list[0] = num1 + num2
        elif arr[i] == '*':
            n_list[0] = num1 * num2
        elif arr[i] == '-':
            n_list[0] = num1 - num2
        elif arr[i] == '/':
            if num1 < 0:
                n_list[0] = -(int(abs(num1)//num2))
            else:
                n_list[0] = int(num1 // num2)

    return n_list[0]

def dfs(cnt):

    global result
    global min_num, max_num

    if cnt == N-1:
        # print(result)
        ans = calc(result)
        min_num = min(ans, min_num)
        max_num = max(ans, max_num)
        return

    for i in range(N-1):

        if visited[i] or (i > 0 and op_str[i-1]==op_str[i] and visited[i-1] == 1):  # 중복 제거
            continue

        result.append(op_str[i])
        # print(result)
        visited[i] = 1
        dfs(cnt+1)
        result.pop()
        visited[i] = 0


N = int(input())    # 수의 개수 (2 ≤ N ≤ 11)
num_list = list(map(int, input().split()))      # 1 ≤ 각각의 수 ≤ 100
op_list = list(map(int, input().split()))   # 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
op = ['+', '-', '*', '/']
op_str = ''
for i in range(4):
    op_str += op[i]*op_list[i]
# print(num_list)
# print(op_str)

max_num = -float('inf')     # 연산결과 최댓값을 담을 변수
min_num = float('inf')      # 연산 결과 최솟값을 담을 변수

visited = [0] * (N-1)
result = []
result_set = ()
dfs(0)

print(max_num)
print(min_num)