# '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
#
# '''
# # 입력을 2차원 배열에 저장하기
# N = int(input())    #배열의 행과 열의 크기
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# print(arr)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# # 0 으로 채워진 3*4 배열 만들기
# arr2 = [[0]*4 for _ in range(N)]
# print(arr2)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# arr2[2][1] = 1
# print(arr2)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
#
# # 이렇게 하면 안됨. for 문 써서 해야함(아래의 얕은복사와 같은 오류 발생)
# arr3 = [[0]*4]*3
# print(arr3)
# arr3[2][1] = 1
# print(arr3) # [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]

'''
2 3
1 2 3
4 5 6
'''
# 2차원 배열의 접근
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')   # 1 2 3 4 5 6

# 2차원 배열의 합
s= 0
for i in range(N):
    for j in range(M):
        s += arr[i][j]
print(s) # 21

# 열 우선 순회
for j in range(M):
    for i in range(N):
        print(arr[i][j], end=' ')   # 1 4 2 5 3 6
        
# 지그재그 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j+(M-1-2*j)*(i % 2)],end=' ')  # 1 2 3 6 5 4
