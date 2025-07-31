def Insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    print(arr)
    
arr = [9, 54, 34, 64, 24]
Insertion_sort(arr)