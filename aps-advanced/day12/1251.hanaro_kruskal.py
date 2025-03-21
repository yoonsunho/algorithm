import sys
sys.stdin = open("txt/1251.txt", "r")

# kruskal로 풀이 .. 간선 위주
# 이 문제 같은 경우 간선의 수가 훨 씬 많기 때문에 kruskal이 prim 보다 오래걸림

def find_set(x):
    if parents[x] == x:
        return x
    
    # 경로 압축 : 시
    # 간 단축
    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x,y):

    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_y == ref_x:
        return

    if ref_y > ref_x:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    E = float(input())
    
    # make_set()
    parents = [i for i in range(N)]
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            cost = ((x_li[i] - x_li[j])**2 + (y_li[i] - y_li[j])**2) * E
            edges.append((i, j, cost))
    # print(edges)
    
    # 비용기준 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    # print(edges)
    
    # 3. 싸이클 검사하면서, 앞에서부터 간선을 연결한다.
    #  - 언제까지 반복? N-1 개의 간선이 선택될 때 까지
    cnt = 0         # 간선 수 담을 변수
    result = 0      # 비용합 담을 변수
    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union_set(u, v)
            cnt += 1
            result += w

        if cnt == N-1:
            break


    print(f'#{tc} {round(result)}')