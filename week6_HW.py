from cs1robots import*

load_world("worlds/maze1.wld")

hubo=Robot(beepers=10)
hubo.set_trace('blue')
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):                       # turn_left 3번 반복
        hubo.turn_left()

# 왼쪽 벽을 따라 이동 하는 함수 정의
def follow_left_wall():
    if hubo.left_is_clear():                # Keep to the left
        hubo.turn_left()
        hubo.move()                          # 한 칸 이동
    elif not hubo.front_is_clear():              # move following the left wall
        turn_back()
    else:
        hubo.move()

def turn_back():
    for i in range(2):
        hubo.turn_left()
# end of definitions

# begin solution
while not hubo.front_is_clear():           # hubo가 처음 위치에서 벽을 만난다면,
 hubo.turn_left()                          # 벽이 없을 때 까지 turn_left
hubo.move()

while not hubo.on_beeper():               #bepper가 없을 경우, follow_left_wall 함수
    follow_left_wall()
