import math
import random
import turtle

gameover = False
turtle.setup(800, 400)
window = turtle.Screen()

def DrawMap():
    drawingTurtle = turtle.Turtle()
    drawingTurtle.hideturtle()
    drawingTurtle.speed(0)

    drawingTurtle.penup()

    for i in range(-100, 200, 100):
        drawingTurtle.penup()
        drawingTurtle.setposition(-400, i)
        drawingTurtle.pendown()
        drawingTurtle.setposition(400, i)

    for i in range(-300, 400, 100):
        drawingTurtle.penup()
        drawingTurtle.setposition(i, 200)
        drawingTurtle.pendown()
        drawingTurtle.setposition(i, -200)


# main
DrawMap()

# 목표물 생성
object = turtle.Turtle()
object.hideturtle()
object.shape("square")
object.resizemode("user")
object.shapesize(1, 1)
object.color("red")
object.penup()

# 주인공 생성
bison = turtle.Turtle()
bison.hideturtle()
bison.shape("turtle")
bison.color("blue")
bison.pendown()
bison.speed(0)

gameover = False

while not gameover:

    # 주인공 위치 초기화
    bison.penup()
    bison.setposition(-380, -180)
    bison.pendown()
    bison.showturtle()

    # 목표물 위치 조정
    randomX = random.randint(10, 390)
    randomY = random.randint(-190, -10)

    # 목표물 테두리
    x1 = randomX - 25
    x2 = randomX + 25
    y1 = randomY + 25
    y2 = randomY - 25

    object.setposition(randomX, randomY)
    object.showturtle()

    # 변수입력받음
    launch_angle = int(input('각도: '))
    r = math.radians(launch_angle)
    launch_velocity = int(input('힘: '))

    for t in range(10000):

        x = launch_velocity * math.cos(r) * 0.5 * t - 380   # x축 이동
        y = launch_velocity * math.sin(r) * 0.5 * t - 0.5 * 9.8 * 0.25 * t ** 2 - 180    # y축 이동 (중력으로 인한 낙하)
        bison.goto(x, y)

        # 물체 테두리에 주인공이 닿았을 경우
        if x1 <= x and x <= x2 and y2 <= y and y <= y1:
            print("win")
            gameover = True
            break

        # 안닿았을 경우
        if x < -400 or x > 400 or y < -200 or y > 200:
            bison.hideturtle()
            object.hideturtle()
            print("try again")
            break

turtle.exitonclick()