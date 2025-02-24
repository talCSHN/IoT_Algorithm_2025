from operator import itemgetter

def makeIndex(arr, pos):
    beforeArr = []
    index = 0
    for data in arr:
        beforeArr.append((data[pos], index))
        index += 1

    sortedArr = sorted(beforeArr, key=itemgetter(0))
    return sortedArr

def bookSearch(arr, data):
    pos = -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if data == arr[mid][0] :
            return arr[mid][1]
        elif data > arr[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

bookArr = [['어린왕자', '쌩뗵쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'], ['신곡', '단테'],
           ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'], ['데미안', '헤르만헤세'], ['파우스트', '괴테'],
           ['대지', '펄벅']]
nameIdx = []
authIdx = []

print(f'## 책장의 도서 -> {bookArr}')
nameIdx = makeIndex(bookArr, 0)
print(f'# 도서명 색인표 -> {nameIdx}')
authIdx = makeIndex(bookArr, 1)
print(f'# 작가명 색인표 -> {authIdx}')

findName = input('도서명 입력 ')
findPos = bookSearch(nameIdx, findName)
if findPos != -1:
    print(f'{findName}의 작가는 {bookArr[findPos][1]} 입니다.')
else:
    print(f'{findName} 책은 없습니다.')

findAuth = input('작가명 입력 ')
findPos = bookSearch(authIdx, findAuth)
if findPos != -1:
    print(f'{findAuth}의 도서는 {bookArr[findPos][0]} 입니다.')
else:
    print(f'{findAuth} 작가는 없습니다.')

