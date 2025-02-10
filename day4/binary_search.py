def binary_search(a, n, key):
    start = 0
    end = n-1
    while start <= end: # 검색 구간의 원소가 1개 이상이면,,(검색구간의 원소가 1개 일 수 있음)
        middle = (start+end)//2     # 기준 위치 계산
        if a[middle] == key:    # 검색 성공!
            return middle
        elif a[middle] > key:   # 중간값이 키보다 크면 왼쪽구간 선택
            end = middle - 1
        else:   # 중간값이 키보다 작으면 오른구간 선택  # a[middle] < key
            start = middle + 1
    return -1   # 검색 구간이 남아있지 않으면, 검색 실패

arr= [2, 4, 7, 9, 11, 19, 23]    # 오름차순 정렬된 배열
print(binary_search(arr, len(arr), 11))     # 4
print(binary_search(arr, len(arr), 4))      # 1
print(binary_search(arr, len(arr), 100))    # -1

