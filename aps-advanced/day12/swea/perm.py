def dfs_permutations(arr):
    # 중복된 순열 피하기 위해 정렬
    arr.sort()

    def dfs(path, used):
        if len(path) == len(arr):
            result.append(path[:])
            return

        for i in range(len(arr)):
            # 방문 여부 및 중복된 순열 피하기
            if used[i] or (i > 0 and arr[i] == arr[i - 1] and not used[i - 1]):
                continue

            used[i] = True
            path.append(arr[i])
            dfs(path, used)
            path.pop()
            used[i] = False

    result = []
    used = [False] * len(arr)
    dfs([], used)

    return result


# 예시 배열
arr = ['+','+','-','/']

# 중복된 순열 생성
unique_perms = dfs_permutations(arr)

# 결과 출력
print(f"중복되지 않은 순열의 개수: {len(unique_perms)}")
print("샘플 순열:")
for perm in unique_perms[:5]:
    print(perm)
