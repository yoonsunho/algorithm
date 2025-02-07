'''
6
2 7 5 3 1 4
'''

N = int(input())
arr = list(map(int, input().split()))

# 배열 원소의 합 s 구하기
s = 0
for i in range(N):
    s += arr[i]
print(s) 

# 배열 원소 중 최댓값 max_v찾기
max_v = arr[0]
for i in range(1, N):
    if arr[i] > max_v:
        max_v = arr[i]
print(max_v)

# 배열 원소 중 최댓값의 max_idx찾기
max_idx = 0
for i in range(1, N):
    if arr[i] > arr[max_idx]:
        max_idx = i
print(max_idx)

# 최댓값이 여러개 인 경우 마지막 인덱스 max_idx 찾기
max_idx = 0
for i in range(1, N):
    if arr[i] >= arr[max_idx]:
        max_idx = i
print(max_idx)

# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기
N, V = map(int, input().split()) #N, 찾는값 V
arr = list(map(int, input().split()))
idx = -1 # 찾는값 없다 가정
for i in range(N):
    if arr[i] == V:
        inx = i # 인덱스 저장
        break # for i