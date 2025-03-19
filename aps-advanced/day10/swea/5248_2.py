import sys
sys.stdin = open("txt/5248.txt", "r")

def make_set(N):

    parents = [i for i in range(N+1)]
    return parents

def find_set(x):    # 조상 찾기

    if parents[x] == x:
        return x

    return find_set(parents[x])

def union_set(x,y):

    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

    # pass
T = int(input())

for tc in range(1,T+1):

    N, M = map(int, input().split())    #  출석번호, 신청서 갯수(2<=N<=100, 1<=M<=100)

    arr = list(map(int, input().split()))

    parents = make_set(N)
    # print(parents)

    for i in range(M):
        union_set(arr[2*i], arr[2*i+1])

    # print(parents)
    # print(len(set(parents)))
    root = set()
    for i in range(1, N+1):
        root.add(find_set(i))

    # print(root)
    # for i in range(N+
    print(f'#{tc} {len(root)}')