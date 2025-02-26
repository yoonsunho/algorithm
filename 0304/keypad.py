def solution(numbers, hand):
    N = len(numbers)  # 숫자의 개수
    result = ['a'] * N  # 결과를 담을 새로운 배열

    cu_l, cu_r = [3, 0], [3, 2]  # 현재 왼손, 오른손의 좌표

    for i in range(N):
        if numbers[i] in [1, 4, 7]:
            cu_l = [numbers[i] // 3, 0]
            result[i] = 'L'
        elif numbers[i] in [3, 6, 9]:
            cu_r = [(numbers[i] - 1) // 3, 2]
            result[i] = "R"
        elif numbers[i] in [2, 5, 8, 0]:
            if numbers[i] == 0:
                num_idx = [3, 1]
            else:
                num_idx = [numbers[i] // 3, 1]

            l_cnt = abs(num_idx[0] - cu_l[0]) + abs(num_idx[1] - cu_l[1])
            r_cnt = abs(num_idx[0] - cu_r[0]) + abs(num_idx[1] - cu_r[1])
            if l_cnt < r_cnt:
                cu_l = num_idx
                result[i] = "L"
            elif l_cnt > r_cnt:
                cu_r = num_idx
                result[i] = "R"
            elif l_cnt == r_cnt:
                if hand == "left":
                    cu_l = num_idx
                    result[i] = "L"
                elif hand == "right":
                    cu_r = num_idx
                    result[i] = "R"

    answer = ''.join(map(str, result))
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))