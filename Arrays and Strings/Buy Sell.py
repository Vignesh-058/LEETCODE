def Max_profit(arr):
    l = 0
    r = 1
    m = 0
    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            if m < profit:
                m = profit
        else:
            l = r
        r+=1
    return m
arr = [7,1,5,3,6,4]
result = Max_profit(arr)
print(result)