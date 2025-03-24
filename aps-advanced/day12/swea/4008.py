import sys
sys.stdin = open("txt/4008.txt", "r")

op = ['+', '-', '*', '/']

def do_count(arr):      # 연산작업 시행

    n_list = num_list[:]
    # print(num_list)
    for i in range(N-1):
        # print(n_list)
        num1 = n_list.pop(0)
        # print(n_list)
        num2 = n_list[0]
        if path[i] == "+":
            n_list[0] = num1 + num2
        elif path[i] == "-":
            n_list[0] = num1 - num2
        elif path[i] == "*":
            n_list[0] = num1 * num2
        elif path[i] == "/":
            n_list[0] = int(num1 / num2)

    # print(num_list[0])
    return n_list[0]

def dfs(cnt):

    global path     # 연산자 순열 담을 리스트
    global min_v, max_v


    if cnt == N-1:
        print(path)
        # print(do_count(path))
        min_v = min(min_v, do_count(path))
        max_v = max(max_v, do_count(path))
        return

    for i in range(N-1):
    
        # 이미 방문 했으면 pass, 중복순열방지
        if visited[i] or (i > 0 and op_li[i] == op_li[i-1] and visited[i-1] == 0):
            continue

        visited[i] = 1
        path.append(op_li[i])
        dfs(cnt+1)
        path.pop()
        visited[i] = 0


T = int(input())
for tc in range(1, T+1):

    N = int(input())    # 숫자의 개수( 3 ≤ N ≤ 12)
    oper = list(map(int, input().split()))      # 연산자는 총 N-1개 있음
    # print(oper)
    op_li = []
    for i in range(4):
        op_li.extend(op[i]*oper[i])

    # print(op_li)
    num_list = list(map(int, input().split()))
    # print(num_list)

    path = []
    visited = [0]*(N-1)
    min_v = float('inf')
    max_v = -float('inf')   # 0 으로 설정하면 안됨 주의 (음수인경우도 있기 때문)
    dfs(0)
    # print(min_v,max_v)
    print(f'#{tc} {max_v-min_v}')