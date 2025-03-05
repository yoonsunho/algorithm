'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

13
2 1 2 3 1 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):      # 전위 순회, 방문한 정점(부모) 먼저 처리
    # global cnt
    if T:   # 0이 아니면, 즉 존재하는 정점(자식)이면
        print(T, end=" ")       # visit[T]에서 할 일 처리
        # cnt += 1
        pre_order(left[T])      # 왼쪽 자식(서브트리)으로 읻동
        pre_order(right[T])     # 오른쪽 자식(서브트리)으로 이동

def in_order(T):
    if T:   # 0이 아니면, 즉 존재하는 정점(자식)이면
        in_order(left[T])  # 왼쪽 자식(서브트리)으로 읻동
        print(T, end=" ")    # visit[T]에서 할 일 처리
        in_order(right[T])  # 오른쪽 자식(서브트리)으로 이동

def post_order(T):      # 후위 순회
    if T:   # 0이 아니면, 즉 존재하는 정점(자식)이면
        post_order(left[T])  # 왼쪽 자식(서브트리)으로 읻동
        post_order(right[T])  # 오른쪽 자식(서브트리)으로 이동
        print(T, end=" ")  # visit[T]에서 할 일 처리


N =int(input())        # 1 번부터 N번까지인 정점
E = N - 1               # 간선 수
arr = list(map(int, input().split()))

left = [0] * (N+1)      # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (N+1)     # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (N+1)       # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i * 2], arr[i*2+1]
    par[c] = p          # 자식을 인덱스로 부모 저장
    if left[p] == 0:    # 왼쪽 자식이 아직 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있는 경우
        right[p] = c


print(left)     # [0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0, 0]
print(right)    # [0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0, 0]

pre_order(1)    # 1 번부터 전위순회
# 1 2 4 7 12 3 5 8 9 6 10 11 13
print()

pre_order(6)    # 6 10 11 13
print()

cnt = 0
# # pre_order(3)    # 3 5 8 9 6 10 11 13
# print()
# print(cnt)      # 8 (순회하는 정점의 개수를 셀 수 있음)

print()
post_order(1)   # 후위순회.. 루트를 마지막에
# 12 7 4 2 8 9 5 10 13 11 6 3 1

print()
# 루트 찾기
root = 1
for i in range(1, N+1):
    if par[i] == 0:     # 부모 정점이 없으면 루트
        root = i
        break
print(root)
pre_order(root)     # 1 2 4 7 12 3 5 8 9 6 10 11 13
# 2 번쨰 테케
# 2 1 4 7 12 3 5 8 9 6 10 11 13