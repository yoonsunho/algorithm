arr = ['A','B','C']
n = len(arr)

def get_sub(tar):
    print(f'target = {tar}',end='/')
    for i in range(n):
        # 0x1 => 비트 연산임을 명시하는 권장 방법
        if tar & 0x1:   # 각 자리의 원소가 포함되어 있나요?
            print(arr[i],end='')
        tar >>= 1       # 맨 우측 비트를 삭제한다
                        # == 다음 원소를 확인하겠다
    # pass

# 전체 부분집합을 확인해야함
for target in range(1 << n):    # 0 1 2 3 4 5 6 7
    # print(target)
    get_sub(target)
    print()