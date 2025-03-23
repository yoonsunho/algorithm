# [0,1,2] 3 개의 카드 존재
# 2개를 뽑을 예정

# 중복 x

path = []       # 뽑은 카드들을 저장
visited = [0] * 7       # 1~6 숫자 사용 여부 기록
# 왜 7개죠? 숫자는 6개 인데?
# -> 그냥 0번 인덱스 안쓰기로 약속(편의를 위해 인덱스 낭비)

# 조금 더 어려운 문제일 경우.. 숫자 범위가 매우 크다
# -> 위와 같은 리스트 방식은 메모리 초과 가능성 존재
# -> dictionary(O(1)), set(O(1)) 이런 자료 구조로 해결

# cnt = 재귀 호출마다 누적되어 전달되어야 하는 값 
def recur(cnt):

    # 카드를 두개 뽑으면 종료((만약 카드 n개 뽑는다면 cnt = n으로 수정)
    if cnt == 2:
        # 종료 시에 해야할 로직 생성
        print(*path)
        return

    # 만약 카드가 1-6까지 6개 있다면?
    for num in range(1, 7):
        # 이미 num을 뽑았다면 뽑지 마라(중복 제거)
        # == num 을 뽑지 않았을 때만 뽑아라
        # if num in path:     # but in 은 시간을 너무 많이 잡아먹음... O(n)
        #     continue
        # path.append(num)
        # recur(cnt + 1)
        # path.pop()

        # 인덱스 검색 연산은 O(1)
        if visited[num]:    # 이미 방문했다면(사용한 수라면)
            continue

        visited[num] = 1
        path.append(num)
        recur(cnt + 1)
        path.pop()
        visited[num] = 0

# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur(0)