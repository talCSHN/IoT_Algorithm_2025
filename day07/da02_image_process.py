# 이미지 처리(정렬 알고리즘)

from tkinter import *

# 앞에 구현한 퀵정렬 코드 그대로 복붙
def sortQuickN(arr, start, end):
    if end <= start: return
        
    low = start; high = end

    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    sortQuickN(arr, start, low - 1)
    sortQuickN(arr, low, end)

# Tkinter 생성
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

# 퀵정렬로 정렬
dataArr = photoArr[:]
sortQuickN(dataArr, 0, len(dataArr)-1)
midValue = dataArr[h*w // 2]

# 색상들을 정리. 중간값보다 작으면 검은색, 중간값보다 크면 흰색
for i in range(len(photoArr)):
    if photoArr[i] <= midValue:
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