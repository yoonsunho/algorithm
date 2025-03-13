arr = ['A','B','C','D','E']
n = len(arr)

# 1 인 bit수를 반환하는 함수
def get_count(tar):
    cnt = 0
    # for _ in range(n):
    #     if tar & 0x1:
    #         cnt += 1
    #     tar >>= 1

    # 같은 코드
    for i in range(n):
        if (tar >> i) & 0x1:
            cnt += 1
    return cnt


# 모든 부분 집합 주 원소의 개수가 2 개 이상인 집합의 수
ans = 0
for target in range(1 << n):    # 0 1 2 3 4 5 6 7
    # 만약, 원소의 개수가 2개 이상이면 answer ++
    if get_count(target) >= 2:
        ans += 1

print(ans)