from tkinter import *

root = Tk()
# 캔버스 밖으로는 그림 못그림
canvas = Canvas(root, width=1000, height=1000, bg='white')
canvas.pack()
# 캔버스 생성 이후

# 1. 기본 원 그리기
# cx = 1000//2
# cy = 1000//2
# r = 400

# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red')

# 전역변수
count = 0
wSize = 1000
radius = 400

# 2. 프랙탈 원 그리기 재귀함수 선언
def drawCircle(x, y, r):
    global count
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.create_text(x, y-r, text=str(count), font=('', 30))

    if r >= radius/2:   # 아직 매개변수로 받는 반지름이 기본 사이즈보다 크면
        drawCircle(x-r//2, y, r//2) # 중심의 왼쪽을 계속 그려감(재귀호출)
        drawCircle(x+r//2, y, r//2) # 중심의 오른쪽을 계속 그려감(재귀호출)

drawCircle(wSize//2, wSize//2, radius)

root.mainloop()