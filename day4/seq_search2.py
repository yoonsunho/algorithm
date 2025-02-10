arr = [[1,2,3],[4,5,6],[7,8,9]]


# 이차원 배열 - 정렬되어 있지 않을 때
def seq_number(arr, n, key):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == key:
                return 1
    return 0


print(seq_number(arr, 3, 5))