import sys
sys.stdin = open("txt/5249.txt", "r")

def find_set(x):

    if x == parents[x]:
        return x

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

    V, E = map(int,input().split())     # 노드 번호 0~V, 간선개수(1<=V<=1000, 1<=E<=1000000)

    parents = [i for i in range(V+1)]

    edges = []      # 정점의 정보와 가중치를 가중치 기준 오름차순으로 담아줄 배열
    for _ in range(E):
        st, end, wei = map(int,input().split())
        edges.append((st,end,wei))

    edges.sort(key=lambda x: x[2])
    # print(edges)

    cnt = 0     # 간선의 개수 담을 변수
    result = 0      # 가중치의 합 담을 변수

    for u, v , w in edges:

        if find_set(u) != find_set(v):
            union_set(u,v)
            cnt += 1
            result += w

        if cnt == V:
            break



    print(f'#{tc} {result}')