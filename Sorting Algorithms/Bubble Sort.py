def Bubble_Sort(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1]=arr[j+1], arr[j]
    print(arr)


arr = [ 9,54,34,64,24 ]
Bubble_Sort(arr)
