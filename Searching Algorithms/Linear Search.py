def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [9, 54, 34, 64, 24]
target = 34
result = Linear_Search(arr, target)
print(result)