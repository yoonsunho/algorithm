# 0421(월)
# 16637.. 괄호 추가하기 (골드3)

def calc(arr):
    sik = susik[:]
    while len(sik) >= 3:
        num1 = int(sik.pop(0))
        oper = sik.pop(0)
        if oper == '+':
            sik[0] = num1 + int(sik[0])
        elif oper == '*':
            sik[0] = num1 * int(sik[0])
        else:
            sik[0] = num1 - int(sik[0])
    return sik[0]

def add_(cnt):

    if cnt == N//2-1:
        print(visited)
        return

    for i in range(1, N//2):

        if visited[i] == 1 or (visited[i] == 0 and visited[i-1] == 1):
            continue

        visited[i] = 1
        add_(cnt+1)
        visited[i] = 0



N = int(input())    # 수식의 길이(1 ≤ N ≤ 19)
susik = list(input())
ans = - float('inf')

num_list = []
oper = []

for i in range(N//2):
    num_list.append(int(susik[2*i]))
    oper.append(susik[2*i+1])
num_list.append(int(susik[-1]))
visited = [0]*(N//2)

add_(0)




