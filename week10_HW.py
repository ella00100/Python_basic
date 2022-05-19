import math   # radius, 삼각 함수 계산을 위해 math 함수 불러옴
from cs1graphics import*  # cs1Graphics 함수 호출
import time   # time 함수 호출 ( time.sleep에 사용)

canvas = Canvas(600, 200)  #Canvas크기(가로,세로)
sun = Circle(30)  # sun 객체 생성 반지름 30인 원
canvas.add(sun)    #sun을 canvas에 추가

def interpolate_colors(t, color1, color2):     # interpolate_colors 함수 정의 (매개변수 t, color1, color2)
                                               # => 색의 그라데이션 변화를 위함
                                               # (r,g,b)=>(255,0,0) : 빨강, (r,g,b)=>(0,255,0) : 초록
    """interpolate between color1(for t ==0.0) and color2(for t==1.0)."""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (int((1-t) * r1 + t * r2),         # 반환 값R
            int((1-t) * g1 + t * g2),
            int((1-t) * b1 + t * b2))

def color_value(color):                      # color_value 함수 정의 (매개변수: color) ColorValue 값 반환
    """Convert a color name to an (r,g,b) tuple."""
    return Color(color).getColorValue()

def animate_sunrise2(sun, morning_sun, noon_sun,morning_sky,noon_sky):  #animate_sunrise2 함수 정의
    # interpolate_colors 함수에 들어갈 색 값 정의 (해/ 하늘)
    morning_color = color_value(morning_sun)   # 아침 색 = 아침 해 컬러 값
    noon_color = color_value(noon_sun)         # 정오 색 = 정오 해의 컬러 값
    dark_sky = color_value(morning_sky)        # 어두운 하늘 = 아침 하늘의 컬러 값
    bright_sky = color_value(noon_sky)         # 밝은 하늘 = 정오 하늘의 컬러 값

    w = canvas.getWidth()   #as befor W~yradius와 동일   ( w= 캔버스 너비, h= 캔버스 높이, r= 해의 반지름)
    h = canvas.getHeight()
    r = sun.getRadius()
    x0 = w/2.0   # 타원 중심 x,y
    y0 = h + r
    xradius = w/2 - r  # 타원 x,y 반지름
    yradius = h

    for angle in range(181):     # 181도 회전 하는 동안 변화
        rad = (angle/180.0) * math.pi   #rad = (각도/180)*pi
        t = math.sin(rad)               #t= sin(rad)
        sun_col = interpolate_colors(t, morning_color, noon_color)  #sun_col= interpolate_colors(t, 아침 색, 정오색)
        sun.setFillColor(sun_col)      #해 내부색 = sun_col
        sky_col = interpolate_colors(t, dark_sky, bright_sky)  #sky_col= interpolate_colors(t, 어두은 하늘, 밝은 하늘)
        canvas.setBackgroundColor(sky_col)  #캔버스색(하늘 색)= sky_col

        x = x0 - xradius * math.cos(rad)    # x,y 좌표의 변화에 따라 해 움직이기
        y = y0 - yradius * math.sin(rad)
        sun.moveTo(x,y)

        time.sleep(0.01)  #시각으로 확인하기 위해 실행 지연

animate_sunrise2(sun, "dark orange", "yellow", "dark blue", "deepskyblue")  #일출일몰 실행