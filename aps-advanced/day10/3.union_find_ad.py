# 6 개의 원소(1~6)이 존재

# 1. 각 집합을 만들어 주는 함수
def make_set(n):
    # 1 ~ n까지의 원소가 잇다 가정 -> 총 n개의 집합 생성
    # --> 각 원소의 부모(!=대표자)를 자신으로 초기화
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1) # rank를 모두 0 으로 초기화
    return parents, ranks

# 대표자 찾기
# def find_set(x):
#     # 자신 == 부모노드 -> 해당 집합의 대표자임
#     if x == parents[x]:
#         return x
#
#     # x의 부모노드를 기준으로 다시 대표자 검색
#     return find_set(parents[x])

# 경로 압축
# def find_set(x):
#     if parents[x] == x:
#         return x
#     # 경로 압축(path compression)을 통해
#     # x의 부모를 대표자로 변경
#     parents[x] = find_set(parents[x])
#
#     return parents[x]

# 경로 압축2(할 때 마다 모든 노드의 대표자를 변경하자)
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]    #  경로 압축
        x = parents[x]


# 합병
def union(x,y):
    
    # 1. x,y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)
    
    # 만약 이미 같은 집합 이라면
    # -> 끝!
    if ref_x == ref_y:
        return 

    # 다른 집합 이라면 합친다
    # -> 문제에 따라 우선되는 집합으로 합쳐주면 됨
    # --> 이번 예시: 더 작은 노드로 합친다
    # if ref_x < ref_y:
    #     parents[ref_y] = ref_x
    # else:
    #     parents[ref_x] = ref_y

    # rank가 작은 쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        # rank가 같으면 한 쪽으로 병합하고, 대표자의 rank 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


N = 6
parents,ranks = make_set(N)
print(parents)  # [0, 1, 2, 3, 4, 5, 6] # 해당 노드(인덱스)의 부모

union(1,3)
union(2,3)
union(5,6)

print(parents)      # [0, 1, 1, 1, 4, 5, 5]

# 3과 5는 같은 집합 인가요??
# if parents[3] == parents[5]  => 이건 대표자가 아닌 부모노드 기준으로 비교하는 것이기 때문에 틀림
if find_set(3) == find_set(5):
    print('같은 집합입니다')
else:
    print('다른 집합 입니다')