t = 'TTTTTATAATA'
p = 'TTA'

def search(p,t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):  # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):  # p에서 비교할 위치 인덱스
            if t[i+j]!= p[j]:
                break
        else:               # break에 걸리지 안고 for가 끝난경우 else실행
            return i        # 패턴이 처음 나타난 인덱스 리턴
    return -1               # t에 패턴 p가 없는 경우

print(search(p,t))