from cs1robots import *                      # 배경 함수 호출

load_world("worlds/amazing5.wld")            # 환경 구성
hubo = Robot(beepers=1, avenue=2, street=1)  # hubo 정의
hubo.set_pause(1)                            # hubo.set 멈춤 시간
hubo.set_trace("blue")                       # hubo.set 색깔

# turn_left를 이용 하여 turn_right 함수 정의
def turn_right():
    for i in range(3):                       # turn_left 3번 반복
        hubo.turn_left()
# 오른쪽 벽을 따라 이동 하는 함수 정의
def follow_right_wall():
    if hubo.right_is_clear():                # Keep to the right
        turn_right()                         # 오른쪽 으로 돌고 (아직 오른쪽이 비어있는 상태)
        hubo.move()                          # 한 칸 이동
    elif hubo.front_is_clear():              # move following the right wall
        hubo.move()
    else:                                    # follow the wall
        hubo.turn_left()
# end of definitions

# begin solution
while not hubo.front_is_clear():           # hubo가 처음 위치에서 벽을 만난다면,
    hubo.turn_left()                       # 벽이 없을 때 까지 turn_left
hubo.drop_beeper()                         # 시작 지점에 drop_beeper
hubo.move()                                # beeper drop 후 바로 beeper 인식을 하지 않도록 한 칸 이동

while not hubo.on_beeper():               #bepper가 없을 경우, follow_right_wall 함수
    follow_right_wall()
