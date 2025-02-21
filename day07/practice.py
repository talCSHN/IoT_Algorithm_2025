import random
import time

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if arr[minIdx] > arr[k]:
                minIdx = k
        temp = arr[i]
        arr[i] = arr[minIdx]
        arr[minIdx] = temp
    
    return arr

def quickSort(arr, start, end):
    if end <= start: return

    low = start
    high = end

    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    quickSort(arr, start, low-1)
    quickSort(arr, low, end)

def quickSortN(arr):
    quickSort(arr, 0, len(arr) - 1)

countArr = [1000, 10000, 12000, 15000]

for count in countArr:
    tempArr = [random.randint(1000, 99999) for _ in range(count)]
    selectArr = tempArr[:]
    quickArr = tempArr[:]

    print(f'## 데이터 수 : {count}개')
    start = time.time()
    selectionSort(selectArr)
    end = time.time()
    # print('선택 정렬 -> %10.3f 초' % (end-start))
    print(f'선택 정렬 -> {end-start:10.3f}초')
    start = time.time()
    quickSortN(quickArr)
    end = time.time()
    # print('퀵 정렬 -> %10.3f 초' % (end-start))
    print(f'선택 정렬 -> {end-start:10.3f}초')
    print()
