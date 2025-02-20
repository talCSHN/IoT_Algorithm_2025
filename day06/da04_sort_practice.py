def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        minIdx = i
        for j in range(i+1, n):
            if arr[minIdx] > arr[j]:
                minIdx = j
        temp = arr[i]
        arr[i] = arr[minIdx]
        arr[minIdx] = temp

    return arr

moneyArr = input('용돈 목록 ').split()
for i in range(len(moneyArr)):
    moneyArr[i] = int(moneyArr[i])


print(f'용돈 정렬 전 -> {moneyArr}')
moneyArr = selectionSort(moneyArr)
print(f'용돈 정렬 후 -> {moneyArr}')
print(f'용돈 중앙값 -> {moneyArr[len(moneyArr)//2]}')