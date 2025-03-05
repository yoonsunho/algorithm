# 완전 이진 트리의 전위 순회
def pre_order(n):
    if n <= N:     # 실존하는 정점이면.. # if T:
        print(n,end=" ")            #     visit(T):
        pre_order(n*2)      #     pre_order(left[T])
        pre_order(n*2+1)    #     pre_order(right[T])

N = 9   # 완전 이진트리 정점 수
tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19]      # 자식의 인덱스에 부모의 정점을 담음

pre_order(1)    # 1 2 4 8 9 5 3 6 7
print()

# 정석
def pre_order(n,N):
    if n <= N:     # 실존하는 정점이면.. # if T:
        print(n,end=" ")            #     visit(T):
        pre_order(n*2,N)      #     pre_order(left[T])
        pre_order(n*2+1,N)    #     pre_order(right[T])

N = 9   # 완전 이진트리 정점 수
tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19]      # 자식의 인덱스에 부모의 정점을 담음

pre_order(1,N)    # 1 2 4 8 9 5 3 6 7