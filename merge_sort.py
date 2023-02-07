import random
# myArray = [21, 4, 1, 3, 9, 20, 25]
myArray = [35, 12, 3, 1, 27, 19]

def mergeSort(list, first, last):
    if (last - first) <= 0:
        return [list[first]]
    
    mid = ((last-first) // 2) + first
    leftHalf = mergeSort(list, first, mid)
    rightHalf = mergeSort(list, mid+1, last)

    arrIndex = first
    leftIndex = rightIndex = 0

    while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
        if leftHalf[leftIndex] <= rightHalf[rightIndex]:
            list[arrIndex] = leftHalf[leftIndex]
            leftIndex += 1
        else:
            list[arrIndex] = rightHalf[rightIndex]
            rightIndex += 1
        
        arrIndex += 1

    while leftIndex < len(leftHalf):
        list[arrIndex] = leftHalf[leftIndex]
        arrIndex += 1
        leftIndex += 1

    while rightIndex < len(rightHalf):
        list[arrIndex] = rightHalf[rightIndex]
        arrIndex += 1
        rightIndex += 1

    return list[first:last+1]

mergeSort(myArray, 0, len(myArray)-1)
print(myArray)
