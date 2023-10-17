import turtle

# 창 설정
window = turtle.Screen()
window.title("마우스로 선 그리기")
window.bgcolor("white")

# 펜 설정
pen = turtle.Turtle()
pen.speed(0)  # 펜 속도 설정 (0: 가장 빠름)
pen.width(3)  # 선의 두께 설정
pen.color("black")

# 마우스 함수
def start_drawing(x, y):
        pen.pendown()
        pen.goto(x, y)

def finish_drawing(x, y):
        pen.penup()
        pen.goto(x, y)

# 'z' 키를 누를 때 이전 선을 지우는 함수
def undo_draw():
    pen.undo()  # 선을 지우고 이전 명령 취소

# 왼쪽, 오른쪽 버튼 클릭에 함수
window.onscreenclick(start_drawing, btn=1)
window.onscreenclick(finish_drawing, btn=3)

# 'z' 키를 누를 때에 함수
window.onkey(undo_draw, "z")
window.listen()

# 창 종료
turtle.done()
