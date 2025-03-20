import sys
sys.stdin = open("graph.txt", "r")

# - 크루스칼
# - 모든 간선들을 보면서
# - 가중치가 작은 간선부터 고르자 (정렬)
# - 이 떄, 싸이클이 발생하면 pass(union find사용)

def find_set(x):    # 대표자 검색
    if x == parents[x]:
        return x
    
    # 기본 코드
    # return find_set(parents[x])

    # 경로 압축 코드드
    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x,y):

    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_y == ref_x:  # 사이클 방지
        return
    
    # 일정한 규칙으로 연결하자
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

V, E = map(int,input().split())
edges = []  # 간선 정보들을 저장할 것임
for _ in range(E):
    st, end, wei = map(int,input().split())
    
    # 간선에 대한 정보들 저장
    edges.append((st,end,wei))

edges.sort(key=lambda x: x[2])  # 가중치 기준으로 오름차순 정렬
# print(edges)

parents = [i for i in range(V)]     # make_set

# 작은것 부터 고르면서 나아가자
# 언제까지? N-1 개를  선택할 떄 까지
cnt = 0     # 현재까지 선택한 간선의 수
result = 0  # MST 가중치의 합

for u,v,w in edges:
    # u와 v가 안결이 안되어 있으면 서택
    # == 다른 집합이라면
    if find_set(u) != find_set(v):
        print(u,v,w)
        union_set(u,v)
        cnt += 1
        result += w

    if cnt == V-1:      # MST구성 끝
        break

print(result)