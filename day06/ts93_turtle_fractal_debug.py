import turtle
import time

def draw_sierpinski_debug(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        return
    
    print(f"Depth: {depth}, Position: ({t.xcor()}, {t.ycor()}), Heading: {t.heading()}")
    
    draw_sierpinski_debug(t, length / 2, depth - 1)
    turtle.update()
    time.sleep(0.1)  # 딜레이 추가
    t.forward(length / 2)
    draw_sierpinski_debug(t, length / 2, depth - 1)
    turtle.update()
    time.sleep(0.1)  # 딜레이 추가
    t.backward(length / 2)
    t.left(60)
    t.forward(length / 2)
    t.right(60)
    turtle.update()
    draw_sierpinski_debug(t, length / 2, depth - 1)
    turtle.update()
    time.sleep(0.1)  # 딜레이 추가
    t.left(60)
    t.backward(length / 2)
    t.right(60)
    turtle.update()

# 설정
turtle.tracer(0)  # 애니메이션 속도 향상
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -100)
t.pendown()

draw_sierpinski_debug(t, 400, 5)

turtle.update()
turtle.done()
