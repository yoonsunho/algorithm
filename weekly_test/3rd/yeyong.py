import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '서울4반_이예영'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 1  # 선공: 0, 후공: 1
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:
    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1]) - 1  # 1 -> 0, 2 -> 1
        print('\n* You will be the %s player. *\n' % ('first' if order == 0 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # 8번 공을 칠 차례인지 확인
    can_hit_8ball = True
    if order == 0:
        other_balls = [1, 3]  # 선공: 1, 3번 공
    else:
        other_balls = [2, 4]  # 후공: 2, 4번 공

    for ball_num in other_balls:
        if balls[ball_num][0] > 0 and balls[ball_num][1] > 0:
            can_hit_8ball = False
            break

    # 목표 공 설정
    if can_hit_8ball:
        target_balls = [5]  # 8번 공
    else:
        if order == 0:
            target_balls = [1, 3]  # 선공: 1, 3번 공
        else:
            target_balls = [2, 4]  # 후공: 2, 4번 공

    # 목표 공 중 가장 가까운 공을 선택
    closest_ball = None
    min_distance = float('inf')
    for target in target_balls:
        if balls[target][0] > 0 and balls[target][1] > 0:
            distance = math.sqrt((balls[target][0] - whiteBall_x) ** 2 + (balls[target][1] - whiteBall_y) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_ball = target

    if closest_ball is not None:
        targetBall_x = balls[closest_ball][0]
        targetBall_y = balls[closest_ball][1]

        # 각도 계산
        width = abs(targetBall_x - whiteBall_x)
        height = abs(targetBall_y - whiteBall_y)

        if whiteBall_x == targetBall_x:
            if whiteBall_y < targetBall_y:
                angle = 0
            else:
                angle = 180
        elif whiteBall_y == targetBall_y:
            if whiteBall_x < targetBall_x:
                angle = 90
            else:
                angle = 270
        else:
            radian = math.atan(width / height) if height > 0 else 0
            angle = 180 / math.pi * radian

        # 사분면에 따라 각도 조정
        if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
            dia = math.sqrt(height ** 2 + width ** 2)
            radian = math.acos((dia ** 2 + height ** 2 - width ** 2) / (2 * dia * height))
            angle = (180 / math.pi * radian) + 180
            current = 3
        # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
        elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
            dia = math.sqrt(height ** 2 + width ** 2)
            radian = math.acos((dia ** 2 + height ** 2 - width ** 2) / (2 * dia * height))
            angle = (180 / math.pi * radian) + 90
            current = 4
        # 목적구가 흰 공을 중심으로 제 2사분면에 위치한 경우 - 코사인 법칙 이용
        elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
            dia = math.sqrt(height ** 2 + width ** 2)
            radian = math.acos((dia ** 2 + width ** 2 - height ** 2) / (2 * dia * width))
            angle = (180 / math.pi * radian) - 90
            current = 2
        # 목적구가 흰 공을 중심으로 제 1사분면에 위치한 경우 - 코사인 법칙 이용
        elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
            dia = math.sqrt(height ** 2 + width ** 2)
            radian = math.acos((dia ** 2 + width ** 2 - height ** 2) / (2 * dia * width))
            angle = (180 / math.pi * radian) - 180
            current = 1

        # 힘의 세기 계산
        distance = math.sqrt(width**2 + height**2)
        power = distance * 0.5

        print(f"공 번호: {closest_ball}, 각도: {angle}, 힘: {power}")

        merged_data = '%f/%f/' % (angle, power)
        sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
