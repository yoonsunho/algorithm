import sys
sys.stdin = open("txt/1244.txt", "r")

# 순열 조합을 만들고..그중 가장 큰 수를 뽑는 방식..?
def swap(count, N):
    global cnt
    global max_v
    global visited

    if count == cnt:
        # print(int("".join(map(str, arr))))
        max_v = max(max_v, int("".join(map(str, arr))))
        return

    # 시간 단축 해야함..
    state = "".join(arr)
    if state in visited:
        return
    visited[state] = 1

    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            visited[i], visited[j] = 1, 1
            swap(count+1, N)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1, T+1):

    num, cnt = input().split()   # 숫자카드
    cnt = int(cnt)

    arr = []    # 숫자 카드를 담을 배열

    for n in num:
        arr.append(n)

    N = len(arr)
    visited = {}

    max_v = 0
    # for i in range(N-1):
    swap(0, N)
    # print(max_v)

    print(f'#{tc} {max_v}')