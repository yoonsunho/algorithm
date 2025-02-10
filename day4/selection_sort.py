def selection_sort(a, N):
    for i in range(N-1):    # 기준위치(최솟값을 찾는 구간의 시작 인덱스)
        min_idx = i         # 최솟값 인덱스 초기화, 구간의 맨 앞 원소를 최소로 가정
        for j in range(i+1,N):
            if a[min_idx] > a[j]:
                min_idx = j
        # if i != min_idx:
        a[i], a[min_idx] = a[min_idx], a[i]
        
    
arr = [10, 25, 64, 22, 11]
selection_sort(arr, len(arr))
print(arr)  # [10, 11, 22, 25, 64]

# k 번째로 작은 원소를 찾는 알고리즘
def select(a, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > arr[j]:
                min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
    return arr[k-1]

print(select(arr,3)) # 22

def select(a,n,k):
    for i in range(n-1):
        min_idx = i
        for j in range(n):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]

