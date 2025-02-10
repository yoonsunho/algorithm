# 정렬이 되어 있는 경우
def seq_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:    # key 값 보다 큰값 나오는 순간 종료(검색 실패)
            return -1
    return -1      # 모든 원소가 KEY보다 작으면

arr = [4, 9, 11, 23, 2, 19, 7]

arr.sort()
print(seq_search(arr, len(arr), 11))    # 4




