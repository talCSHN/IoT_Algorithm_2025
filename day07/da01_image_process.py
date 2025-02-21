# 이미지 처리

from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('이미지 처리')

photo = PhotoImage(file='./image/cupdog.png')

photoArr = []
h = photo.height()  # 600
w = photo.width()   # 600
for i in range(h):  # 행렬 row와 동일
    for k in range(w):  # 행렬 col과 동일
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3    # 평균치
        photoArr.append(value)

print(len(photoArr))    # 360,000개 리스트 생성

# 색상들을 정리. 127보다 작으면 검은색, 127보다 크면 흰색
for i in range(len(photoArr)):
    if photoArr[i] < 127:
        photoArr[i] = 0 # black
    else:
        photoArr[i] = 255   # white

# 흑백이미지로 변경
pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoArr[pos]
        pos += 1
        photo.put(f'#{r:02x}{g:02x}{b:02x}', (i,k)) # photo 각 위치의 색상을 흑백으로 photoArr에 들어있는 값으로 변경

paper = Label(root, image=photo)
paper.pack(expand=1, anchor=CENTER)

root.mainloop()