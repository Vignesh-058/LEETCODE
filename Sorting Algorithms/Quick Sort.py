import random;
def Quick_Sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return Quick_Sort(left)+mid+Quick_Sort(right)

arr = [3,42,23,66,4,56,6]
result=Quick_Sort(arr)
print(result)