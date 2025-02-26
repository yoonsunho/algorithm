import sys

sys.stdin = open("flatten.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 강사님 풀이
    dump = int(input())
    box_heights = list(map(int, input().split()))

    for _ in range(dump):  # 이 for문은 반복문에 불과하기 때문에 _ 사용

        max_idx, max_box_height = 0, box_heights[0]
        min_idx, min_box_height = 0, box_heights[0]

        for i in range(len(box_heights)):
            # 최댓값 찾기
            if box_heights[i]> max_box_height:
                max_idx, max_value = i, box_heights[i]

            # 최솟값 찾기
            if box_heights[i]< min_box_height:
                min_idx, min_box_height = i, box_heights[i]

        # 평탄화 높이 차이가 1 이하라면 굳이 평탄화를 할 필요가 없음
        if max_box_height - min_box_height <= 1:
            break


        box_heights[max_idx] -= 1
        box_heights[min_idx] += 1

    # 평탄화가 끝나고 나서도, 또 최대 높이의 상자와 최소 높이의 상자가 바뀌었을 수도 있다.
    print(f'{test_case} {max(box_heights) - min(box_heights)}')